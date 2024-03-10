
# Use the following command to set your OpenWeatherMap API key:
# cmd
# Copy code:
# setx OPENWEATHERMAP_API_KEY "your_actual_api_key"
# Please note not willling to put the notebook version to show app running as not willing to show api key (yes, i know there ways i can hide it)
# code for educational purposes only 

import requests
import os

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENWEATHERMAP_API_KEY")

# Check if the API key is available
if not api_key:
    print("Error: API key not found. Set the OPENWEATHERMAP_API_KEY environment variable.")
    exit()

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather information for a city
def get_weather(city):
    # Construct the API request URL
    request_url = f"{base_url}?appid={api_key}&q={city}"

    # Make the API request
    response = requests.get(request_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Extract relevant weather information from the JSON data
        weather_description = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)

        # Display the weather information in a user-friendly format
        print(f"Weather in {city.capitalize()}:")
        print(f"- Description: {weather_description}")
        print(f"- Temperature: {temperature}°C")
    else:
        # Display an error message based on the specific error returned by the API
        error_message = data.get('message', 'An error occurred')
        print(f"Error: {error_message}")

# Main function
def main():
    # Get user input for the city
    city = input("Enter a City Name: ").strip()

    # Validate the input
    if not city:
        print("Error: City name cannot be empty.")
        exit()

    # Get and display the weather information
    get_weather(city)

if __name__ == "__main__":
    main()
