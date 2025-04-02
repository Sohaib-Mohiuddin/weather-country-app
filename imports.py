import requests # for making HTTP requests
import json # for parsing JSON data
import os # for file operations
import time # for time operations
import logging # for logging
from dotenv import load_dotenv # for loading environment variables
import datetime # for date and time operations
from rich.console import Console # for rich console output
from rich.table import Table # for rich table output
from rich.progress import Progress # for progress bar
from prompt_toolkit import prompt # for user input
from prompt_toolkit.completion import WordCompleter # for autocompletion
from prompt_toolkit.styles import Style # for styling
from colorama import Fore, Style as ColoramaStyle, init # for colored output