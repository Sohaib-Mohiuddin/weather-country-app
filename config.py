exec(open("imports.py").read())

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Initializing Colorama and Console for pretty printing
init(autoreset=True)
console = Console()

# API Constants
RESTCOUNTRIES_API_URL = 'https://restcountries.com/v3.1/all'
OWM_API_URL='https://api.openweathermap.org/data/2.5/weather'
OPEN_METEO_API_URL='https://api.open-meteo.com/v1/forecast'
HISTORY_STORAGE_FILE = 'weather_history.json'
CUSTOM_STYLE = Style.from_dict({
    'prompt': 'ansicyan bold',
    'question': 'ansigreen',
    'input': 'ansiyellow'  
})

# Retreiving Country Data for automcompletion
with console.status("[bold green]Retrieving country data...") as status:
    try:
        response = requests.get(RESTCOUNTRIES_API_URL)
        response.raise_for_status()
        countries_data = response.json()
        countries = { country['name']['common'].lower(): country for country in countries_data }
        country_names = list(countries.keys())
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error retrieving country data: {e}")
        exit(1)
        
# Autocompletion for country names
country_completer = WordCompleter(country_names, ignore_case=True)