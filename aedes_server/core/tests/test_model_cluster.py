from datetime import datetime

from django.test import TestCase
from ..models import Cluster


class ClusterModelTest(TestCase):
    def setUp(self):
        self.cluster = Cluster.objects.create(
            label=1,
            latitude=-22.5,
            longitude=-43.1,
        )

    def test_cluster_exists(self):
        '''Cluster instances should be correctly created.'''
        self.assertTrue(Cluster.objects.exists())

    def test_cluster_date(self):
        '''Instances should contain a created_at date.'''
        self.assertIsInstance(self.cluster.created_at, datetime)
