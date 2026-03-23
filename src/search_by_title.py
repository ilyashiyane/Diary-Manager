import json 
import os
from rich.console import Console
from dotenv import load_dotenv 
from rich.text import Text

def SearchByTitle(name) :
        load_dotenv()
        console=Console()
        diaries_path=os.getenv("DIARIES_PATH")
        with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
        demande_title=Text("Please provide the title of the diary you want to search for : ",style="bold yellow")
        title = console.input(demande_title)
        for diary in journal:
                    if diary["Title"].lower() == title.lower():
                        print(f"Date: {diary['Date']}")
                        print(f"Title: {diary['Title']}")
                        print(f"Text: {diary['Text']}")