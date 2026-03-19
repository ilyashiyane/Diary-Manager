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
            console.print(Align("What do you want ?",align="center",style="italic green"))
            print("1.Press 1 to view  all diarie's title")
            print("2.Press 2 to view all diaries ")
            choice=int(input("Give your choice"))
            if choice==1 :
              for diary in journal:
                console.print(Align(f"[italic green] Title:[/italic green] {diary['Title']}",align="center"))
            elif choice==2 :
              for diary in journal:
                console.print(Align(f"[italic green] Title:[/italic green] {diary['Title']}",align="center"))
                console.print(Align(f"[italic green] Date:[/italic green] {diary['Date']}",align="center"))
                console.print(Align(f"[italic green] Text: [/italic green]{diary['Text']}",align="center"))
            
    