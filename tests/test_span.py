# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
import unittest
from datetime import datetime

from dateutil.relativedelta import relativedelta

from gallus_decoder_tools.errors import HarnessError
from gallus_decoder_tools.span import date_span


class DateSpanTests(unittest.TestCase):
    def test_leap_year_span(self) -> None:
        result = date_span("2020-01-01", "2021-01-01")
        self.assertEqual(result["total_days"], 366)
        self.assertEqual(result["years"], 1)
        self.assertEqual(result["months"], 0)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["weeks"], 52)
        self.assertEqual(result["extra_days"], 2)
        self.assertEqual(result["breakdowns"]["years_days"], "1 Year, 0 Days")
        self.assertEqual(result["breakdowns"]["years_months_days"], "1 Year, 0 Months, 0 Days")
        self.assertEqual(result["breakdowns"]["weeks_days"], "52 Weeks, 2 Days")
        self.assertEqual(result["breakdowns"]["months_days"], "12 Months, 0 Days")
        self.assertEqual(result["century_percent"], "1.00%")
        self.assertEqual(result["millennium_percent"], "0.10%")
        self.assertFalse(result["reordered"])

    def test_short_leap_span_and_same_day(self) -> None:
        short = date_span("02/28/2020", "03/01/2020")
        self.assertEqual(short["total_days"], 2)
        self.assertEqual(short["breakdowns"]["years_months_days"], "2 Days")
        same = date_span("June 15, 2020", "June 15, 2020")
        self.assertEqual(same["total_days"], 0)
        self.assertEqual(same["breakdowns"]["years_months_days"], "0 Days")
        inclusive = date_span("2020-06-15", "2020-06-15", include_end=True)
        self.assertEqual(inclusive["total_days"], 1)
        self.assertEqual(inclusive["breakdowns"]["years_months_days"], "1 Day")

    def test_reorders_and_parses_day_first_when_needed(self) -> None:
        result = date_span("03/01/2020", "31/01/2020")
        self.assertEqual(result["start"], "2020-01-31")
        self.assertEqual(result["end"], "2020-03-01")
        self.assertTrue(result["reordered"])
        self.assertEqual(date_span("01/02/2020", "01/02/2020")["start"], "2020-01-02")

    def test_month_end_matches_calendar_delta(self) -> None:
        start = datetime(2019, 1, 31)
        end = datetime(2019, 3, 1)
        result = date_span(start, end)
        delta = relativedelta(end, start)
        self.assertEqual((result["years"], result["months"], result["days"]), (delta.years, delta.months, delta.days))
        self.assertEqual(result["total_days"], (end - start).days)

    def test_bad_date(self) -> None:
        with self.assertRaises(HarnessError):
            date_span("tomorrow", "2020-01-01")


if __name__ == "__main__":
    unittest.main()
