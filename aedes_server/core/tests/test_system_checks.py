from django.conf import settings
from django.test import TestCase
from ..apps import CoreConfig
from ..checks import check_threshold, check_aws_credentials


class ThresholdSystemCheckTest(TestCase):
    def setUp(self):
        # Removing THRESHOLD from settings
        delattr(settings, 'THRESHOLD')
        self.errors = check_threshold(CoreConfig)

    def test_threshold_missing(self):
        '''Error list should not be empty'''
        self.assertNotEqual(0, len(self.errors))

    def test_treshold_error_code(self):
        '''Error code must be e_001.'''
        self.assertEqual('aedes.e_001', self.errors[0].id)

    def tearDown(self):
        # Re-adding THRESHOLD to settings
        setattr(settings, 'THRESHOLD', 0.0005)


class AWSSystemCheckTest(TestCase):
    def setUp(self):
        self._original_id = settings.AWS_ACCESS_KEY_ID
        self._original_secret = settings.AWS_SECRET_ACCESS_KEY
        self._original_buck = settings.AWS_STORAGE_BUCKET_NAME

        delattr(settings, 'AWS_ACCESS_KEY_ID')
        delattr(settings, 'AWS_SECRET_ACCESS_KEY')
        delattr(settings, 'AWS_STORAGE_BUCKET_NAME')

        self.errors = check_aws_credentials(CoreConfig)

        def test_credentials_missing(self):
            '''Error list should not be empty'''
            self.assertNotEqual(0, len(self.errors))

        def test_credentials_error_code(self):
            '''Error code must be e_002.'''
            self.assertEqual('aedes.e_002', self.errors[0].id)
