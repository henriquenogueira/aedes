from django.shortcuts import resolve_url as r
from django.test import TestCase


class ClustersTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:clusters'))

    def test_status_code(self):
        '''GET clusters page should return 200.'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''GET clusters page should render cluster.html'''
        self.assertTemplateUsed(self.resp, 'clusters.html')

    def test_context(self):
        '''GET clusters page should have cluster context.'''
        self.resp
