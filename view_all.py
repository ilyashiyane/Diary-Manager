import json
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

def ViewAll(name):
    console=Console()
    load_dotenv()
    diaries_path=os.getenv("DIARIES_PATH")
    try:
            with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
    except FileNotFoundError:
                console.print(Align("No diaries found.",align="center",style="bold red"))
    if not journal:
                console.print(Align("No diaries found.",align="center",style="bold red"))
    else:
            for diary in journal:
                console.print(Align(f"Title: {diary['Title']}",align="center",style="italic green"))
                console.print(Align(f"Date: {diary['Date']}",align="center"))
                console.print(Align(f"Text: {diary['Text']}",align="center"))
                