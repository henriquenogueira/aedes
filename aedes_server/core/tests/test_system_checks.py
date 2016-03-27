from django.conf import settings
from django.test import TestCase
from ..apps import CoreConfig
from ..checks import check_threshold


class SystemCheckTest(TestCase):
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
