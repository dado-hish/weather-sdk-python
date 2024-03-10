import unittest
from unittest.mock import patch, MagicMock
from weather_sdk import WeatherSDK

class TestWeatherSDK(unittest.TestCase):
    def setUp(self):
        self.sdk = WeatherSDK(api_key="f29ad15e026d87f3cef4b175e704cc46")

    @patch('weather_sdk.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 273.15},
            'visibility': 10000,
            'wind': {'speed': 1},
            'dt': 1710098686,
            'sys': {'sunrise': 1710040750},
            'timezone': 10800,
            'name': 'Cheboksary'
        }
        mock_get.return_value = mock_response

        data = self.sdk.get_weather("London")
        self.assertTrue('weather' in data)

    @patch('weather_sdk.requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {'message': 'City not found'}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            self.sdk.get_weather("NonexistentCity")

if __name__ == '__main__':
    unittest.main()
