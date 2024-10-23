# Weather Checking Application

This is a Python-based command-line application that allows users to check the weather for different cities. It utilizes the WeatherAPI to fetch real-time weather information and offers the following features:

## Features

- Check current weather by city.
- Add your favorite cities for quick weather checks.
- Remove cities from your favorites list.
- Display the list of your favorite cities.
- Auto-refresh weather information every 15 seconds.

## Requirements

- Python 3.x
- `requests` library: Install it via `pip install requests`
- A valid API key from [WeatherAPI](https://www.weatherapi.com/)

## Setup

1. Clone this repository to your local machine:

   git clone https://github.com/kalithasanks2001/Weather-Checking-App.git

2. Navigate into the project directory:

   cd Weather-Checking-App

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Replace the placeholder API key in the script with your own API key from [WeatherAPI](https://www.weatherapi.com/).

   Open the `Weather.py` file and replace the following line:

   ```python
   API_KEY = 'c851881264344e7ca2353350240601'
   ```

## Usage

1. To check the weather for a specific city, run the script and use the `get_weather_by_city()` function:

   ```bash
   python Weather.py
   ```

2. Use the available functions to manage your favorite cities:
   - Add a city to your favorites.
   - Remove a city from your favorites.
   - Toggle auto-refresh mode for automatic updates every 15 seconds.

## Example

```python
# Example usage in interactive Python environment
get_weather_by_city('New York')
```

## Contributing

Feel free to submit issues and pull requests if you want to contribute to this project.
