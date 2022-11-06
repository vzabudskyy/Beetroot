"""
"dfe60b1bcb6bc9a7fcee386d50120eca"
"""
import requests
from datetime import datetime
import json


ddcit = {'base': 'stations',
         'clouds': {'all': 99},
         'cod': 200,
         'coord': {'lat': 50.4333, 'lon': 30.5167},
         'dt': 1667320198,
         'id': 703448,
         'main': {'feels_like': 280.5,
                  'humidity': 64,
                  'pressure': 1007,
                  'temp': 281,
                  'temp_max': 282.38,
                  'temp_min': 280.22},
         'name': 'Kyiv',
         'sys': {'country': 'UA',
                 'id': 2003742,
                 'sunrise': 1667278088,
                 'sunset': 1667313287,
                 'type': 2},
         'timezone': 7200,
         'visibility': 10000,
         'weather': [{'description': 'overcast clouds',
                      'icon': '04n',
                      'id': 804,
                      'main': 'Clouds'}],
         'wind': {'deg': 179, 'gust': 1.39, 'speed': 1.37}}


class WeatherApp:
    def __init__(self):
        self.__api = "YOUR_API_KEY"
        self.__forecast = None

    @staticmethod
    def get_weather_data(country, city):
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/"
                               f"weather?q={city},{country}&"
                               f"APPID=dfe60b1bcb6bc9a7fcee386d50120eca")
        return json.loads(weather.text)

    def produce_forecast(self, weather: dict):
        dt = datetime.utcfromtimestamp(weather["dt"])
        date = dt.strftime("%d-%m-%Y")
        time = dt.strftime("%H:%M:%S")
        weather_type = f"{weather['weather'][0]['main']}, {weather['weather'][0]['description']}"
        temp = round(weather["main"]["temp"] - 273)
        humidity = f"{weather['main']['humidity']}%"
        cloudness = f"{weather['clouds']['all']}%"
        self.__forecast = f"Date: {date}\n" \
                          f"Time: {time}\n" \
                          f"Weather: {weather_type}\n" \
                          f"Temperature: {temp}C\n" \
                          f"Humidity: {humidity}\n" \
                          f"Cloudness: {cloudness}"

    def __str__(self):
        json_weather = app.get_weather_data("ua", "Kyiv")
        self.produce_forecast(json_weather)
        return self.__forecast


if __name__ == "__main__":
    app = WeatherApp()
    print(app)
