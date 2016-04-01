from datetime import datetime, timedelta, timezone

from aedes_server.tests.utils import generate_test_image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from ..models import Report


class ReportModelTest(TestCase):
    def setUp(self):
        self.report = Report.objects.create(
            latitude=-22.5,
            longitude=-43.1,
            device_id='DEVICE ID #123',
            category='C'
        )

    def test_report_exists(self):
        '''Report instances should be correctly created.'''
        self.assertTrue(Report.objects.exists())

    def test_report_date(self):
        '''Instances should contain a report date.'''
        self.assertIsInstance(self.report.reported_at, datetime)

    def test_report_date_auto_now(self):
        '''Reported_at should contain current timestamp.'''
        self.assertLess(datetime.now(timezone.utc) + timedelta(seconds=-5), self.report.reported_at)

    def test_device_id(self):
        '''Make sure there is a Device ID on row'''
        self.assertTrue(hasattr(self.report, 'device_id'))

    def test_device_str(self):
        '''Device ID should be a string'''
        self.assertIsInstance(self.report.device_id, str)

    def test_comment_none(self):
        '''Comment should be None'''
        self.assertEqual('', self.report.comment)

    def test_has_resolved_flag(self):
        '''Reports should have default flag set to False by default.'''
        self.assertEqual(False, self.report.resolved)


class PhotoModelTest(TestCase):
    def setUp(self):
        # Creating report entry
        self.report = Report(
            latitude=-22.5,
            longitude=-43.1,
            device_id='DEVICE ID #123',
            category='C',
            photo=self._generate_photo()
        )

        self.report.photo.name = self.report.photo.name.split('/')[-1]
        self.report.save()

    def test_photo_exists(self):
        '''Photo should exist'''
        self.assertIsNotNone(self.report.photo)

    def tearDown(self):
        """Cleaning temporary files"""

        # Removing from storage
        storage, path = self.report.photo.storage, self.report.photo.name
        storage.delete(path)

        # Removing database entry
        self.report.delete()

    def _generate_photo(self):
        '''
        Auxiliary method that generates a random image
        '''

        tmp_file = generate_test_image()

        img = SimpleUploadedFile(
            name=tmp_file.name,
            content=open(tmp_file.name, 'rb').read(),
            content_type='image/jpeg'
        )
        return img
