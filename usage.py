from weather_sdk import WeatherSDK

def main():
    sdk = WeatherSDK(api_key="f29ad15e026d87f3cef4b175e704cc46")
    city = input("Enter city name: ")
    try:
        data = sdk.get_weather(city)
        print(data)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
