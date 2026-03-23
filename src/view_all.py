import json
import os
import questionary
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from questionary import Style
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
            custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # jaune + bold
])
            choice = questionary.select(
    "What would you like to do?",
    choices=[
        "📄 View all diary titles",
        "📚 View all diaries"
    ],
    style=custom_style
).ask()
            
            if choice=="📄 View all diary titles":
              for diary in journal:
                console.print(Align(f"[italic green] Title:[/italic green] {diary['Title']}",align="center"))
                console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice=="📚 View all diaries" :
              for diary in journal:
                console.print(Align(f"[italic green] Title:[/italic green] {diary['Title']}",align="center"))
                console.print(Align(f"[italic green] Date:[/italic green] {diary['Date']}",align="center"))
                console.print(Align(f"[italic green] Text: [/italic green]{diary['Text']}",align="center"))
                console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            
    