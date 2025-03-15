import requests as rq # For site requests
import os # To clean console
from workWithDB import Database # For work with DB
from config import DB_CONFIG # Config for DB

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

def mainMenuUser(nickname):
    print('q')

def choiseSourceInformation(nickname):
    print('q')