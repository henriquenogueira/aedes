from django.test import TestCase
from django.core.management import call_command
from ..models import Report, Cluster


class CustomCommandTest(TestCase):
    def setUp(self):
        Report.objects.create(latitude=-22.0003, longitude=-43.0001, category='F')
        Report.objects.create(latitude=-22.0004, longitude=-43.0001, category='C')
        Report.objects.create(latitude=-22.0003, longitude=-43.0002, category='S')
        Report.objects.create(latitude=-26.0003, longitude=-60.0001, category='F')
        Report.objects.create(latitude=-26.0004, longitude=-60.0001, category='C')
        Report.objects.create(latitude=-26.0005, longitude=-60.0002, category='S')
        Report.objects.create(latitude=-12.0003, longitude=-23.0001, category='F')
        Report.objects.create(latitude=-12.0004, longitude=-23.0001, category='C')
        Report.objects.create(latitude=-12.0005, longitude=-23.0002, category='S')

    def test_update_clusters(self):
        '''Compute cluster command should create clusters on database.'''
        call_command('compute_clusters')
        self.assertEqual(5, Cluster.objects.count())
