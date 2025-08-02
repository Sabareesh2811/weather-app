import requests

# Replace with your real OpenWeatherMap API key
API_KEY = "your_api_key_here"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("\nCity not found. Please check the spelling.")

# Ask the user for a city name
city_name = input("Enter a city name: ")
get_weather(city_name)
