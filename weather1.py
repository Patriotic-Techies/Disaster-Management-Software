import requests
from datetime import datetime

def get_weather_report(api_key, location):
    weatherstack_url = "http://api.weatherstack.com/current"
    weather_params = {
        'access_key': api_key,
        'query': location,
    }

    try:
        weather_response = requests.get(weatherstack_url, params=weather_params)
        weather_data = weather_response.json()

        if 'current' in weather_data:
            weather = weather_data['current']
            temperature = weather['temperature']
            weather_description = weather['weather_descriptions'][0]
            humidity = weather['humidity']
            wind_speed = weather['wind_speed']
            wind_direction = weather['wind_dir']
            pressure = weather['pressure']
            uv_index = weather['uv_index']
            visibility = weather['visibility']
            cloud_cover = weather['cloudcover']
            sunrise = weather_data['location']['localtime'][11:16]
            #sunset = data['location']['sunset'][11:16]

            print(f"Weather report for {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {weather_description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")
            print(f"Wind Direction: {wind_direction}")
            print(f"Atmospheric Pressure: {pressure} hPa")
            print(f"UV Index: {uv_index}")
            print(f"Visibility: {visibility} km")
            print(f"Cloud Cover: {cloud_cover}%")
            print(f"Sunrise: {sunrise}")
            #print(f"Sunset: {sunset}")

            abnormal_conditions = ["storm", "tornado", "heavy rain"]
            if any(keyword in weather_description.lower() for keyword in abnormal_conditions):
                print("ALERT: Abnormal weather conditions detected!")
            else:
                print("Weather is normal.")

        else:
            print(f"Error: Unable to retrieve weather data for {location}")


        # Example: Earthquake alerts using the USGS API
        earthquake_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        earthquake_response = requests.get(earthquake_url)
        earthquake_data = earthquake_response.json()
        if 'features' in earthquake_data:
            print("Earthquake alert: There are recent earthquakes in the area.")
        # Example: Add checks for other disaster types here

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    location = input("Enter the name of the location: ")
    api_key = "77303b1ba466691b387c09fe08dd7ee2"  
    get_weather_report(api_key, location)

