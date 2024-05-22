from weather_forecast import WeatherForecast

# Main method which handles user input from the command line
def main():
    while True:
        weather_app = WeatherForecast()
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ") # Take input from user for which city they'd like to know the weather for
        if (city.lower() == 'exit'):
            break # Exit loop if specified by user

        detailed = input("Do you want a detailed forecast? (yes/no): ").lower() # Take input from user about detailed or simple response
        if detailed == 'yes':
            weather_app.display_detailed_weather(city)
        else:
            weather_app.display_weather(city)

if __name__ == "__main__":
    main()