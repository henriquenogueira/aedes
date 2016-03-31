from django.shortcuts import resolve_url as r
from django.test import TestCase
from ..models import Report


class LatestViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:latest'))

    def test_status_code(self):
        '''GET /latest/ should return 200.'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''GET /latest/ should render latest.html'''
        self.assertTemplateUsed(self.resp, 'latest.html')

    def test_context(self):
        '''View should have "latest" in context.'''
        self.assertIn('latest', self.resp.context)

    def test_context_type(self):
        '''The context "latest" should contain reports.'''
        queryset = self.resp.context['latest']
        self.assertEqual(Report, queryset.model)
