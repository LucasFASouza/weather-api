import unittest
import json
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_get_weather_by_city(self):
        response = self.client.get('/weather/?city=Sao%20Paulo')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('city', data)

    def test_get_weather_by_coordinates(self):
        response = self.client.get('/weather/?lat=-23.5475&lon=-46.6361')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('city', data)

    def test_get_weather_without_city_or_coordinates(self):
        response = self.client.get('/weather/')
        self.assertEqual(response.status_code, 400)

    def test_get_weather_with_incomplete_coordinates(self):
        response = self.client.get('/weather/?lat=-23.5475')
        self.assertEqual(response.status_code, 400)

    def test_get_logs(self):
        response = self.client.get('/logs/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
