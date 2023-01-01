import os
import datetime
import requests
import boto3
from chalice import Chalice, Rate
from dotenv import load_dotenv

app = Chalice(app_name='temperature-tracker')

load_dotenv()

# Set the environment variables for the OpenWeatherMap API key and location
OWM_API_KEY = os.environ['OWM_API_KEY']
LOCATION = os.environ['LOCATION']

# Set the URL for the OpenWeatherMap API
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={OWM_API_KEY}'

# Set the name of the S3 bucket and the key for the text file
BUCKET_NAME = 'weather48'
FILE_KEY = 'temperature.txt'

# Create an S3 client
s3 = boto3.client('s3')

@app.route("/")
def get_temperature():
    # Make a request to the OpenWeatherMap API
    response = requests.get(API_URL)
    data = response.json()

    # Get the temperature from the API response
    temperature = data['main']['temp']

    # Convert the temperature from Kelvin to Celsius
    temperature = temperature - 273.15
    
    #  Get the current time and format it as a string
    now = datetime.datetime.now()
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')

    # Concatenate the temperature and time strings
    temperature_str = f'{temperature:.1f}°C, {time_str}'
    return {"temp": temperature_str}

@app.schedule(Rate(1, unit=Rate.MINUTES))  # Run this function every minute
def save_temperature():
    # Make a request to the OpenWeatherMap API
    response = requests.get(API_URL)
    data = response.json()

    # Get the temperature from the API response
    temperature = data['main']['temp']

    # Convert the temperature from Kelvin to Celsius
    temperature = temperature - 273.15
    
    #  Get the current time and format it as a string
    now = datetime.datetime.now()
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')

    # Concatenate the temperature and time strings
    temperature_str = f'{temperature:.1f}°C, {time_str}'

    # Save the temperature to a text file in S3
    s3.put_object(Bucket=BUCKET_NAME, Key=FILE_KEY, Body=temperature_str)