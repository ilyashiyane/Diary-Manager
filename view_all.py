import json
import os
from dotenv import load_dotenv
def ViewAll(name):
    load_dotenv()
    diaries_path=os.getenv("DIARIES_PATH")
    try:
            with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
    except FileNotFoundError:
                print("No diaries found.")
    if not journal:
                    print("No diaries found.")
    else:
            for diary in journal:
                print(f"Date: {diary['Date']}")
                print(f"Title: {diary['Title']}")
                print(f"Text: {diary['Text']}")