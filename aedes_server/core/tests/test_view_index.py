from django.shortcuts import resolve_url as r
from django.test import TestCase


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'))

    def test_response_code(self):
        '''GET / should return 200.'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''GET / should render map.html.'''
        self.assertTemplateUsed(self.resp, 'map.html')

    def test_page_title(self):
        '''Page title should be Aedespot.'''
        self.assertContains(self.resp, '<title>Aedespot</title>')

    def test_map_is_present(self):
        '''Map should be displayed on index.'''
        self.assertContains(self.resp, 'id="map"')

    def test_about_modal(self):
        '''About modal should be present.'''
        self.assertContains(self.resp, 'id="aboutModal"')
