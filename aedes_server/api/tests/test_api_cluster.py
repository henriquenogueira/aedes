from aedes_server.core.models import Cluster
from django.shortcuts import resolve_url as r
from rest_framework import test, status


class ReportListApiTest(test.APITestCase):
    def setUp(self):
        self.fixture = (
            {'label': 1, 'latitude': 22, 'longitude': 43},
            {'label': 2, 'latitude': 23, 'longitude': 42}
        )
        for d in self.fixture:
            Cluster.objects.create(**d)
        self.resp = self.client.get(r('api:cluster-list'))

    def test_list_exists(self):
        '''GET on reports endpoint should return 200.'''
        self.assertEqual(self.resp.status_code, status.HTTP_200_OK)

    def test_list_content(self):
        '''Response should contain all values created.'''
        self.assertEqual(len(self.fixture), len(self.resp.data))
