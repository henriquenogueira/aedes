from django.shortcuts import resolve_url as r
from rest_framework import test, status


class ReportCreateApiTest(test.APITestCase):
    def test_report_create(self):
        '''POST requests on endpoint with valid data should create object.'''
        data = {'latitude': 22, 'longitude': 43, 'category': 'F', 'device_id': 'DEVICE 1'}
        self.assertCodeForData(data, status.HTTP_201_CREATED)

    def test_report_create_error_type(self):
        '''Wrong type of data on POST request should return 400.'''
        data = {'latitude': '', 'longitude': 43, 'category': 'F'}
        self.assertCodeForData(data, status.HTTP_400_BAD_REQUEST)

    def test_report_create_error_missing(self):
        '''Missing data on POST request should return 400.'''
        data = {'latitude': '', 'longitude': 43}
        self.assertCodeForData(data, status.HTTP_400_BAD_REQUEST)

    def test_report_create_error_device_missing(self):
        '''Report should contain a device ID'''
        data = {'latitude': 22, 'longitude': 43, 'category': 'F'}
        self.assertCodeForData(data, status.HTTP_400_BAD_REQUEST)

    def assertCodeForData(self, data, expected_code):
        '''
        Auxiliary method for asserting requests status codes
        based on sent data.
        '''
        response = self.client.post(r('api:report-list'), data, format='json')
        self.assertEqual(response.status_code, expected_code)


class ReportListApiTest(test.APITestCase):
    def setUp(self):
        self.fixture = (
            {'latitude': 22, 'longitude': 43, 'category': 'F', 'device_id': 'DEVICE 1'},
            {'latitude': 23, 'longitude': 42, 'category': 'C', 'device_id': 'DEVICE 2'}
        )
        for d in self.fixture:
            self.client.post(r('api:report-list'), d, format='json')
        self.resp = self.client.get(r('api:report-list'))

    def test_list_exists(self):
        '''GET on reports endpoint should return 200.'''
        self.assertEqual(self.resp.status_code, status.HTTP_200_OK)

    def test_list_content(self):
        '''Response should contain all values created.'''
        self.assertEqual(len(self.fixture), len(self.resp.data))
