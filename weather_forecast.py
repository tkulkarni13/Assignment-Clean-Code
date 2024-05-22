# WeatherForecast module which handles displaying weather data based on input city
class WeatherForecast:
    # Constructor
    def __init__(self):
        # More data for more cities can be added here to expand the available weather data
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
    
    # Function to display weather in a particular city
    def display_weather(self, city):
        if (city not in self.weather_data.keys()):
            print(f"Weather data not available for {city}") # Notify user if no data is available
        else:
            weather = self.weather_data.get(city, {})
            print(f"Weather in {city}: {weather["condition"]}") # Display only the condition
    
    # Function to display all weather data about a particular city
    def display_detailed_weather(self, city):
        if (city not in self.weather_data.keys()):
            print(f"Weather data not available for {city}") # Notify user if no data is available
        else:
            weather = self.weather_data.get(city, {})
            # Display all data available about input city
            print(f"Weather in {city}: {weather["temperature"]} degrees, {weather["condition"]}, Humidity: {weather["humidity"]}%")