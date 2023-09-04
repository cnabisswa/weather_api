import requests


def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"weather in {city}:")

        print(f"temperature: {temperature} degree celcius:")
        print(f"humidity: {humidity} %")
        print(f"description: {weather_desc.capitalize()}")
    else:
        print("city not found. Please check the city name and try again.")


if__name__ = "__main__"
api_key = "db7cc3faa133632d89a295cde1a83c93"
city_name = input("ENTER CITY NAME:")

get_weather(city_name, api_key)