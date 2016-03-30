import shutil
import tempfile

from django.conf import settings
from django.test.runner import DiscoverRunner


class TempMediaMixin(object):
    '''Mixin to create MEDIA_ROOT in temp and tear down when complete.'''

    def setup_test_environment(self):
        '''Create temp directory and update MEDIA_ROOT and default storage.'''
        super().setup_test_environment()
        self._temp_media = tempfile.mkdtemp()

        # Creating place holders
        settings._original_media_root = settings.MEDIA_ROOT
        settings._original_file_storage = settings.DEFAULT_FILE_STORAGE

        # Settings storage for tests
        settings.MEDIA_ROOT = self._temp_media
        settings.DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    def teardown_test_environment(self):
        '''Delete temp storage.'''
        super().teardown_test_environment()
        shutil.rmtree(self._temp_media, ignore_errors=True)

        # Setting original settings
        settings.MEDIA_ROOT = settings._original_media_root
        settings.DEFAULT_FILE_STORAGE = settings._original_file_storage

        # Removing placeholders
        del settings._original_media_root
        del settings._original_file_storage


class LocalTestSuiteRunner(TempMediaMixin, DiscoverRunner):
    '''Local test suite runner.'''
    pass
