# import functions as f 

# # nick = "user1"
# city = 'Lipetsk'

# f.clearConsole()
# # #print('Welcome to app for weather analysis!')
# # # f.enterCityName()
# f.getWeatherCity_WeatherApi(city)

import user as u

def main():
    user = u.User("Alice")
    user.login()

def check(us):
    trueOr = us.check_status()
    print(trueOr)

# main()
user_instance = u.User("Alice")
user_instance.login()
check(user_instance)

# Завершить работу с классом User