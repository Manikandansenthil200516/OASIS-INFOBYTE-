import requests

def get_weather_data(city_name):
    """
    Fetches and returns the current weather data for the specified city.
    """
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    """
    Displays the current weather data for the specified city.
    """
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]

        weather_desc = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature}K")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_desc}")
    else:
        print("City not found!")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_data = get_weather_data(city_name)
    display_weather_data(weather_data)