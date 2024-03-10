import time
import requests


class WeatherSDK:
    def __init__(self, api_key, mode='on-demand'):
        self.api_key = api_key
        self.mode = mode
        self.cities_data = {}
        self.max_cached_cities = 10

    def get_weather(self, city):
        if not city:
            raise ValueError("City name cannot be empty")

        if city not in self.cities_data or (time.time() - self.cities_data[city]['timestamp']) > 600:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
            response = requests.get(url)
            response_json = response.json()
            if response.status_code == 200:
                if len(self.cities_data) >= self.max_cached_cities:
                    oldest_city = min(self.cities_data, key=lambda k: self.cities_data[k]['timestamp'])
                    del self.cities_data[oldest_city]  # Remove the oldest cached city
                self.cities_data[city] = {'data': response_json, 'timestamp': time.time()}
                return self.transform_weather_data(response_json)
            else:
                raise Exception(f"Failed to fetch weather data: {response_json.get('message', 'Unknown error')}")
        else:
            return self.cities_data[city]['data']

    def set_mode(self, mode):
        if mode not in ['on-demand', 'polling']:
            raise ValueError("Invalid mode. Valid modes are 'on-demand' and 'polling'")
        self.mode = mode

    def transform_weather_data(self, original_data):
        transformed_data = {}

        if 'weather' in original_data and isinstance(original_data['weather'], list) and len(
                original_data['weather']) > 0:
            transformed_data['weather'] = {
                'main': original_data['weather'][0].get('main', ''),
                'description': original_data['weather'][0].get('description', '')
            }
        else:
            transformed_data['weather'] = {
                'main': '',
                'description': ''
            }

        if 'main' in original_data:
            transformed_data['temperature'] = {
                'temp': original_data['main'].get('temp', 0),
                'feels_like': original_data['main'].get('feels_like', 0)
            }

        if 'wind' in original_data:
            transformed_data['wind'] = original_data['wind']

        if 'visibility' in original_data:
            transformed_data['visibility'] = original_data['visibility']

        if 'dt' in original_data:
            transformed_data['datetime'] = original_data['dt']

        if 'sys' in original_data:
            transformed_data['sys'] = {
                'sunrise': original_data['sys'].get('sunrise', 0),
                'sunset': original_data['sys'].get('sunset', 0)
            }

        if 'timezone' in original_data:
            transformed_data['timezone'] = original_data['timezone']

        if 'name' in original_data:
            transformed_data['name'] = original_data['name']

        return transformed_data


if __name__ == "__main__":
    api_key = 'f29ad15e026d87f3cef4b175e704cc46'
    sdk = WeatherSDK(api_key, 'on-demand')
    city = 'Moscow'
    weather_data = sdk.get_weather(city)
    print(weather_data)


