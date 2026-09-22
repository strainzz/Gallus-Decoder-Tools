# SPDX-License-Identifier: LicenseRef-Gallus-Labs-Noncommercial
# Copyright 2026 Gallus Labs
"""Calendar span between two dates."""

from __future__ import annotations

import calendar
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from gallus_decoder_tools.errors import HarnessError
from gallus_decoder_tools.numbers import _fibonacci_fast, _nth_prime

_FORMATS = (
    "%m/%d/%Y",
    "%m-%d-%Y",
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%d-%m-%Y",
    "%m/%d/%y",
    "%d/%m/%y",
    "%B %d, %Y",
    "%b %d, %Y",
)


def _plural(count: int, word: str) -> str:
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def parse_date(value: object) -> datetime:
    """Parse a calendar date. Slash dates are month/day/year unless the first number is past 12."""
    if isinstance(value, datetime):
        return value.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    text = str(value).strip()
    if not text:
        raise HarnessError("Provide a date.")

    formats = list(_FORMATS)
    if "/" in text and not text.startswith(("19", "20")):
        parts = text.split("/")
        if len(parts) == 3:
            try:
                if int(parts[0]) > 12 and int(parts[1]) <= 12:
                    formats.insert(0, "%d/%m/%Y")
                    if len(parts[2]) == 2:
                        formats.insert(0, "%d/%m/%y")
            except ValueError:
                pass

    for fmt in formats:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    raise HarnessError(
        f"Could not parse date: {text}. Use MM/DD/YYYY, YYYY-MM-DD, or Month D, YYYY."
    )


def date_numerology(date: datetime) -> dict:
    """Return DN1 through DN4 for one calendar date.

    DN1 adds every digit in the month, day, and year.
    DN2 keeps the month and day whole, then adds the year digits.
    DN3 adds the month, the day, and the last two year digits as one number.
    DN4 adds the month, the day, the first two year digits, and the last two.
    """
    month, day, year = date.month, date.day, date.year
    year_text = str(year)
    year_prefix = int(year_text[:2])
    year_suffix = int(year_text[2:])
    digit_text = f"{month}{day}{year}"
    year_digit_sum = sum(int(digit) for digit in year_text)
    dn1 = sum(int(digit) for digit in digit_text)
    dn2 = month + day + year_digit_sum
    dn3 = month + day + year_suffix
    dn4 = month + day + year_prefix + year_suffix
    steps = {
        "dn1": " + ".join(digit_text) + f" = {dn1}",
        "dn2": f"{month} + {day} + {' + '.join(year_text)} = {dn2}",
        "dn3": f"{month} + {day} + {year_suffix} = {dn3}",
        "dn4": f"{month} + {day} + {year_prefix} + {year_suffix} = {dn4}",
    }
    named = (("DN1", dn1, steps["dn1"]), ("DN2", dn2, steps["dn2"]), ("DN3", dn3, steps["dn3"]), ("DN4", dn4, steps["dn4"]))
    day_of_year = date.timetuple().tm_yday
    days_in_year = 366 if calendar.isleap(year) else 365
    return {
        "date": date.strftime("%Y-%m-%d"),
        "month": month,
        "day": day,
        "year": year,
        "day_of_year": day_of_year,
        "days_in_year": days_in_year,
        "days_remaining": days_in_year - day_of_year,
        "month_day_year": f"{month}/{day}/{year}",
        "day_month_year": f"{day}/{month}/{year}",
        "joined_month_day_year": int(digit_text),
        "joined_day_month_year": int(f"{day}{month}{year}"),
        "dn1": dn1,
        "dn2": dn2,
        "dn3": dn3,
        "dn4": dn4,
        "steps": steps,
        "breakdown": [
            {
                "name": name,
                "value": value,
                "steps": step,
                "prime": _nth_prime(value),
                "triangular": value * (value + 1) // 2,
                "fibonacci": _fibonacci_fast(value),
                "square": value * value,
            }
            for name, value, step in named
        ],
    }


def _parse_include_end(value: object) -> bool:
    if value is None or value is False:
        return False
    if value is True:
        return True
    if isinstance(value, str):
        text = value.strip().lower()
        if text in {"1", "true", "yes"}:
            return True
        if text in {"0", "false", "no", ""}:
            return False
    raise HarnessError("include_end must be true or false.")


def date_span(start: object, end: object, include_end: object = False) -> dict:
    """Measure the calendar distance from start to end.

    The earlier date is placed first. ``include_end`` counts the end date as a full day.
    """
    start_date = parse_date(start)
    end_date = parse_date(end)
    inclusive = _parse_include_end(include_end)
    reordered = False
    if end_date < start_date:
        start_date, end_date = end_date, start_date
        reordered = True

    measured_end = end_date + timedelta(days=1) if inclusive else end_date
    total_days = (measured_end - start_date).days
    delta = relativedelta(measured_end, start_date)
    years = delta.years
    months = delta.months
    days = delta.days

    date_after_years = start_date + relativedelta(years=years)
    days_after_years = (measured_end - date_after_years).days
    weeks_after_years, days_after_weeks_and_years = divmod(days_after_years, 7)
    total_weeks, extra_days = divmod(total_days, 7)
    total_months = years * 12 + months

    if years == 0:
        years_days = f"0 Years, {_plural(days, 'Day')}"
    else:
        years_days = f"{_plural(years, 'Year')}, {_plural(days_after_years, 'Day')}"

    if years == 0 and months == 0:
        years_months_days = _plural(days, "Day")
    elif years == 0:
        years_months_days = f"{_plural(months, 'Month')}, {_plural(days, 'Day')}"
    else:
        years_months_days = (
            f"{_plural(years, 'Year')}, {_plural(months, 'Month')}, {_plural(days, 'Day')}"
        )

    return {
        "start": start_date.strftime("%Y-%m-%d"),
        "end": end_date.strftime("%Y-%m-%d"),
        "start_display": start_date.strftime("%B %d, %Y"),
        "end_display": end_date.strftime("%B %d, %Y"),
        "include_end": inclusive,
        "reordered": reordered,
        "total_days": total_days,
        "years": years,
        "months": months,
        "days": days,
        "weeks": total_weeks,
        "extra_days": extra_days,
        "century_percent": f"{(total_days / 36525) * 100:.2f}%",
        "millennium_percent": f"{(total_days / 365250) * 100:.2f}%",
        "breakdowns": {
            "years_days": years_days,
            "years_months_days": years_months_days,
            "years_weeks_days": (
                f"{_plural(years, 'Year')}, "
                f"{_plural(weeks_after_years, 'Week')}, "
                f"{_plural(days_after_weeks_and_years, 'Day')}"
            ),
            "months_days": f"{_plural(total_months, 'Month')}, {_plural(days, 'Day')}",
            "weeks_days": f"{_plural(total_weeks, 'Week')}, {_plural(extra_days, 'Day')}",
        },
        "numerology": {
            "start": date_numerology(start_date),
            "end": date_numerology(end_date),
        },
    }
