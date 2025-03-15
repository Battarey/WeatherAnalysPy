import requests as rq # For site requests
import os # To clean console
import time as t # To sleep function
from workWithDB import Database # For work with DB
from config import API_KEY # Api key for openweathermap
from config import DB_CONFIG # Config for DB

# Попробовать сделать авторизацию через айпи или аккаунт
# Для запоминания по IP в SQL можно использовать Exists  

def clearConsole():
    os.system('cls')
    
def authorization():
    db = Database(DB_CONFIG)
    db.connect()
    try:
        rows = db.execute_query("SELECT * FROM Users")
        for row in rows:
            print(row) 
    except Exception as e:
        print(f"An error occurred during the authorization process: {e}")
    finally:
        db.close()

def mainMenu():
    print('q')

def enterCityName():
    city = input("Enter the city name: ")
    boolAnswer = getWeatherCity(city)
    pressEnter = input('\nPress Enter to go to the main menu'), clearConsole, mainMenu()
def enterCitiesName():
    print('Enter names separated by commas, no more than 5, otherwise the app itself will reduce it to 5')
    cities_input = input('Enter the cities name: ')
    cities = [city.strip() for city in cities_input.split(",")][:5]
    for city in cities:
        print(f'\nGetting weather for {city}:')
        getWeatherCity(city)
    pressEnter = input('\nPress Enter to go to the main menu'), clearConsole, mainMenu()
def enterCountryName():
    print('As an output, the weather in the country will display the weather in the main cities of the country you selected.')
    print('Countries to choose from: RU, UK, DE, ES, IT')
    choiseCountry = input('')
    if choiseCountry.upper() == 'RU':
        print('You have chosen Russia!')
        citiesOfCountry = ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Nizhny Novgorod']
    elif choiseCountry.upper() == 'UK':
        print('You have chosen United Kindom!')
        citiesOfCountry = ['London', 'Birmingham', 'Manchester', 'Glasgow', 'Liverpool']
    elif choiseCountry.upper() == 'DE':
        print('You have chosen Germany!')
        citiesOfCountry = ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Cologne']
    elif choiseCountry.upper() == 'ES':
        print('You have chosen Spain!')
        citiesOfCountry = ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza']
    elif choiseCountry.upper() == 'IT':
        print('You have chosen Italy!')
        citiesOfCountry = ['Rome', 'Milan', 'Naples', 'Turin', 'Florence']
    else: 
        print('Not correct input! Try again!'), t.sleep(4), clearConsole(), enterCountryName()

    for city in citiesOfCountry:
        print(f"\nGetting weather for {city}, {choiseCountry.upper()}:")
        getWeatherCity(city)
    
    pressEnter = input('\nPress Enter to go to the main menu'), clearConsole, mainMenu()

def getWeatherCity(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = rq.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("City not found. Please check the name you entered.")


def choiseSourceInformation(nickname):
    print('q')