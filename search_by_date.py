import json 
import os
from dotenv import load_dotenv


#try:
            #with open(f"C:/Users/Lenovo/Desktop/Mydiary/Diaries/{name}.json", "r", encoding="utf-8") as file:
               # journal = json.load(file)
#except FileNotFoundError:
                #journal = []

def SearchByDate(name):
    load_dotenv()
    diaries_path=os.getenv("DIARIES_PATH")
    with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
    dat = input("Please provide a date in this format: year-month-day (YYYY-MM-DD). ")
    for diary in journal:
                    if diary["Date"].startswith(dat):
                        print(f"Date: {diary['Date']}")
                        print(f"Title: {diary['Title']}")
                        print(f"Text: {diary['Text']}")