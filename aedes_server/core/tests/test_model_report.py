from datetime import datetime

from django.test import TestCase
from ..models import Report


class ReportModelTest(TestCase):
    def setUp(self):
        self.report = Report.objects.create(
            latitude=-22.5,
            longitude=-43.1,
            category='C'
        )

    def test_report_exists(self):
        '''Report instances should be correctly created.'''
        self.assertTrue(Report.objects.exists())

    def test_report_date(self):
        '''Instances should contain a report date.'''
        self.assertIsInstance(self.report.reported_at, datetime)
