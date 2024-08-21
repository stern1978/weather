#!/usr/bin/python3

import requests
import datetime
import json
import config


weather_url = 'https://api.openweathermap.org/data/2.5/forecast?' + config.lat_lon + '&units=imperial&cnt=4&appid=' + config.weather_api
weather_get = requests.get(weather_url)
weather_data = weather_get.json()
    
forecast_list = []
day_counter = 0
daily = weather_data['list']


try:
    for _ in daily:
        forecast_day = datetime.datetime.fromtimestamp(weather_data['list'][day_counter]['dt']).strftime('%a %-I:%M%p')
        forecast_max = round(weather_data['list'][day_counter]['main']['temp'])
        forecast_min = round(weather_data['list'][day_counter]['main']['temp_min'])
        forecast_icon = "/static/png/" + weather_data['list'][day_counter]['weather'][0]['icon'] + ".png"
        forecast_description = weather_data['list'][day_counter]['weather'][0]['main']
        forecast_pop = round(weather_data['list'][day_counter]['pop'] * 100)
        avg_temp = (forecast_max + forecast_min) / 2

        try:
            forecast_rain = round(weather_data['list'][day_counter]['rain']['3h'] / 25.4, 2)
        except KeyError:
            forecast_rain = 0.00
        try:
            if avg_temp in range(28, 35):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 10, 2)
            elif avg_temp in range(20, 28):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 15, 2)
            elif avg_temp in range(15, 20):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 20, 2)
            elif avg_temp in range(10, 15):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 30, 2)
            elif avg_temp in range(0, 10):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 40, 2)
            elif avg_temp in range(-20, 0):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 50, 2)
            elif avg_temp in range(-100, -20):
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 100, 2)
            else:
                forecast_snow = round(weather_data['list'][day_counter]['snow']['3h'] / 25.4 * 1, 2)
        except KeyError:
            forecast_snow = 0.00
        

        day_dict = {'forecast_day': forecast_day,
                    'forecast_max': forecast_max,
                    'forecast_min': forecast_description,
                    'forecast_icon': forecast_icon,
                    'forecast_pop': forecast_pop,
                    'forecast_rain': forecast_rain,
                    'forecast_snow': forecast_snow}

        day_list = (forecast_day, forecast_max, forecast_description, forecast_icon, forecast_pop, forecast_rain, forecast_snow)
        forecast_list.append(day_list)
        day_counter += 1

except IndexError:
    pass

try:
    with open('/home/pi/Documents/weather/forecast.json', 'w', encoding='utf-8') as f:
        json.dump(forecast_list, f, ensure_ascii=False, indent=4)
except FileNotFoundError as e:
    print(e)

