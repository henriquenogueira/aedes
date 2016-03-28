from django.test import TestCase
from django.core.management import call_command
from ..models import Report, Cluster


class CustomCommandTest(TestCase):
    def setUp(self):

        # Building dataset for test
        keys = ('latitude', 'longitude', 'category')
        data = (
            (-22.0003, -43.0002, 'F'),
            (-22.0004, -43.0001, 'C'),
            (-22.0003, -43.0002, 'S'),
            (-26.0003, -60.0001, 'F'),
            (-26.0004, -60.0001, 'C'),
            (-26.0005, -60.0002, 'S'),
            (-12.0003, -23.0001, 'F'),
            (-12.0004, -23.0001, 'C'),
            (-12.0005, -23.0002, 'S'),
        )

        # Creating database rows for dataset
        for point in data:
            args = dict(zip(keys, point))
            Report.objects.create(**args)


    def test_update_clusters(self):
        '''Compute cluster command should create clusters on database.'''
        call_command('compute_clusters')
        self.assertEqual(3, Cluster.objects.count())
