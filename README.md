# Weather SDK

Weather SDK - это инструментарий разработки программного обеспечения (SDK) для доступа к данным о погоде с использованием API OpenWeatherMap.

## Установка

Вы можете установить Weather SDK с помощью pip:

```bash
pip3 install weather-sdk-nikita-alekseev
```

```python
from weather_sdk import WeatherSDK

# Создаем экземпляр WeatherSDK с вашим API-ключом
sdk = WeatherSDK(api_key="your_openweathermap_api_key")

# Получаем данные о погоде для города London
data = sdk.get_weather("London")

# Выводим данные о погоде
print(data)
```

