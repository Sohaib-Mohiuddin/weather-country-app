'''
Author: Sohaib Mohiuddin
Course: ENGR5200G - Professor Qusay Mahmoud

Description: This script is a command-line weather application that allows users to check the current weather and historical data for a specific city in a given country. It uses the OpenWeatherMap API to fetch weather data and displays it in a user-friendly format. The script also includes error handling for invalid inputs and network issues. This script also utlizes Open-Meteo API to fetch historical weather data for the same day and RESTCOUNTRIES API to fetch country data for autocompletion.
'''

# Importing necessary libraries from the imports.py file

from weather_functions import *

if __name__ == "__main__":
    console.print('[bold green]🌍 Welcome to the Weather App![/bold green]')
    console.print('[bold yellow]Type "no" to quit the application after your first run.[/bold yellow]')
    try:
        while True:
            country = prompt("🌍 Enter country name: ", completer=country_completer, style=CUSTOM_STYLE).strip().lower()
            if country.lower() == "no":
                console.print("[bold red]Exiting the application...[/bold red]")
                break
            if country.lower() not in countries:
                console.print(f"[bold red]Invalid country. Please try again.[/bold red]")
                continue
            
            city = prompt("🏙️ Enter city name: ", style=CUSTOM_STYLE)
            weather_data, lat, lon = fetch_weather(city, country)
            
            if weather_data and lat and lon:
                historical_data = get_historical_data(lat, lon)
                display(weather_data, historical_data, city, country)
            
            continue_prompt = prompt("Do you want to check another city? (yes/no): ", style=CUSTOM_STYLE).strip().lower()
            if continue_prompt == "no":
                console.print("[bold red]Exiting the application...[/bold red]")
                break
            elif continue_prompt != "yes":
                console.print("[bold yellow]Invalid input. Please enter 'yes' or 'no'.[/bold yellow]")
                continue
            
            console.print("[bold green]Thank you for using the Weather App![/bold green]")
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting the application...[/bold red]")
    except EOFError:
        console.print("\n[bold red]Exiting the application...[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
    finally:
        console.print("[bold yellow]Goodbye![/bold yellow]")