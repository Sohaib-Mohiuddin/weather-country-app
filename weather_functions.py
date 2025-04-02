from config import *

def fetch_weather(city, country):
    """Fetches weather data for a given city and country."""
    
    console.print(f"\n[bold cyan]Fetching weather for {city}, {country}...[/bold cyan]")
    params = {
        'q': f"{city},{country}",
        'appid': os.getenv('OWM_API_KEY'),
        'units': 'metric'
    }
    try:
        # Using Progress bar for fetching weather data
        with Progress() as progress:
            task = progress.add_task("[cyan]Retrieving weather data...", total=100)
            response = requests.get(OWM_API_URL, params=params)
            response.raise_for_status()
            progress.update(task, advance=100)
        
        data = response.json()
        weather_data = {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }
        
        # Extract latitude and longitude
        lat, lon = data["coord"]["lat"], data["coord"]["lon"]
        
        return weather_data, lat, lon
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching weather data: {e}")
        return None, None, None

def get_historical_data(lat, lon):
    """Fetches historical weather data for a given latitude and longitude for the same day."""
    
    today = datetime.date.today().isoformat()
    console.print(f"\n[bold cyan]Fetching historical weather data on {today} for {lat}, {lon}...[/bold cyan]")
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "past_days": 1,  # Ensures we get historical data from today
        "timezone": "auto"
    }
    
    try:
        # Using Progress bar for fetching historical data
        with Progress() as progress:
            task = progress.add_task("[cyan]Retrieving historical weather data...", total=100)
            response = requests.get(OPEN_METEO_API_URL, params=params)
            response.raise_for_status()
            progress.update(task, advance=100)
        
        data = response.json()
        
        historical_data = [
            (time, temp) for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])
            if time.startswith(today)  # Filter for today's date
        ]
        
        # historical_data = list(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
        
        return historical_data
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching historical data: {e}")
        return None

def display(weather_data, historical_data, city, country):
    """Displays weather data in a formatted table."""
    
    table = Table(title=f"Weather in {city}, {country}", title_justify="left")
    table.add_column("Metric", justify="right", style="cyan")
    table.add_column("Value", justify="left", style="magenta")
    
    table.add_row("Temperature", f"{weather_data['temperature']} °C")
    table.add_row("Feels Like", f"{weather_data['feels_like']} °C")
    table.add_row("Humidity", f"{weather_data['humidity']}%")
    table.add_row("Condition", f"{weather_data['condition'].title()}")
    
    console.print(table)
    
    # Display historical data if available
    if historical_data:
        console.print("\n[bold cyan]Historical Weather Data:[/bold cyan]")
        historical_table = Table(title=f"Historical Weather Data for {city}, {country}", title_justify="left")
        historical_table.add_column("Time", justify="right", style="cyan")
        historical_table.add_column("Temperature (°C)", justify="left", style="magenta")
        
        for time, temp in historical_data:
            historical_table.add_row(time, f"{temp} °C")
        
        console.print(historical_table)