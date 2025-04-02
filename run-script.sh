# Script to automate run of 1 or more Python scripts
# Usage: ./run-script.sh

file="country_weather_app.py"

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install it to run this script."
    exit
fi

# Check if the virtual environment exists and is activated
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating a new one..."
    python3 -m venv .venv
fi
source .venv/bin/activate

echo "Virtual environment activated."

# Check if the required packages are installed and if not installed then install from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
else
    echo "Warning: requirements.txt not found. Skipping dependency installation."
fi

# Check if the script file exists
if [ ! -f "$file" ]; then
    echo "Script file $file not found."
    exit 1
fi

# Run the script
echo "Running $file..."
python3 "$file"
if [ $? -eq 0 ]; then
    echo "$file executed successfully."
else
    echo "Error occurred while executing $file."
fi