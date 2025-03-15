import requests as rq # For site requests
import os # To clean console
import time as t # To sleep function
from workWithDB import Database # For work with DB
from config import API_KEY_OpenWeatherMap # Api key for openweathermap
from config import API_KEY_WeatherApi # Api key for weatherapi
from config import DB_CONFIG # Config for DB

# Попробовать сделать авторизацию через айпи или аккаунт
# Для запоминания по IP в SQL можно использовать Exists  

def clearConsole():
    os.system('cls')
    
def authorization():
    choise = ('Do you want to log in? 1 - yes, 2 - no')
    if choise == '1':
        # sql requery for login

        print('')
    elif choise == '2':
        # sql requery for ip
        clearConsole(), mainMenu()
    else:
        print('Incorreect input! Try again!'), t.sleep(4), clearConsole(), authorization()

    # db = Database(DB_CONFIG)
    # db.connect()
    # try:
    #     rows = db.execute_query("SELECT * FROM Users")
    #     for row in rows:
    #         print(row) 
    # except Exception as e:
    #     print(f"An error occurred during the authorization process: {e}")
    # finally:
    #     db.close()

def choiseSourceInformation():
    print('Select where you want your data supplied from:')
    print('1 - Open Weather Map')
    print('2 - Weather Api')
    choise = input('Your choise: ')
    if choise == '1':
        api = 'open'
        print('You chose Open Weather Map! Lets go!'), t.sleep(4), clearConsole(), mainMenu(api)
    elif choise == '2':
        api = 'weather'
        print('You chose Open Weather Map! Lets go!'), t.sleep(4), clearConsole(), mainMenu(api)
    else: 
        print('Incorrect input! Try again!'), t.sleep(4), clearConsole(), choiseSourceInformation()

def mainMenu(api):
    print('Choise your operation:')
    print('1 - Displaying information about one city')
    print('2 - Displaying information about several cities')
    print('3 - Displaying information about the main cities of the country')
    choise = input('Your choise: ')
    if choise == '1':
        enterCityName(api)
    elif choise == '2':
        enterCitiesName(api)
    elif choise == '3':
        enterCountryName(api)
    else:
        print('Incorrect input! Try again!'), t.sleep(4), clearConsole, mainMenu(api)

def enterCityName(api):
    city = input("Enter the city name: ")
    if api == 'open':
        getWeatherCity_OpenWeather(city)
    elif api == 'weather':
        getWeatherCity_WeatherApi(city)
    else:
        print('Error app!'), t.sleep(4), clearConsole(), choiseSourceInformation()
    pressEnter = input('\nPress Enter to go to the main menu'), clearConsole, mainMenu()
def enterCitiesName(api):
    print('Enter names separated by commas, no more than 5, otherwise the app itself will reduce it to 5')
    cities_input = input('Enter the cities name: ')
    cities = [city.strip() for city in cities_input.split(",")][:5]
    if api == 'open':
        for city in cities:
            print(f'\nGetting weather for {city}:')
            getWeatherCity_OpenWeather(city)
    elif api == 'weather':
            print(f'\nGetting weather for {city}:')
            getWeatherCity_WeatherApi(city)
    else:
        print('Error app!'), t.sleep(4), clearConsole(), choiseSourceInformation()
    pressEnter = input('\nPress Enter to go to the main menu'), clearConsole, mainMenu()
def enterCountryName(api):
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
    
    if api == 'open':
        for city in citiesOfCountry:
            print(f"\nGetting weather for {city}, {choiseCountry.upper()}:")
            getWeatherCity_OpenWeather(city)
    elif api == 'weather':
            print(f"\nGetting weather for {city}, {choiseCountry.upper()}:")
            getWeatherCity_WeatherApi(city)
    else:
        print('Error app!'), t.sleep(4), clearConsole(), choiseSourceInformation()

    pressEnter = input('\nPress Enter to go to the main menu'), clearConsole, mainMenu()

def getWeatherCity_OpenWeather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_OpenWeatherMap}&units=metric"
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
def getWeatherCity_WeatherApi(city): 
    base_url = 'http://api.weatherapi.com/v1/current.json'
    url = f'{base_url}?key={API_KEY_WeatherApi}&q={city}'
    response = rq.get(url)

    if response.status_code == 200:
        data = response.json() 

        location = data['location']['name']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        print(f'Weather at {location}: {temperature}°C, {condition}')
    else:
        print(f'Error {response.status_code}: {response.text}')