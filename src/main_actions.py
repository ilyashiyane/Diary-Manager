import json
import os
import questionary
from dotenv import load_dotenv
from rich.console import Console 
from rich.panel import Panel
from rich.align import Align
from questionary import Style
def main_actions(name): 
    console = Console()
    #load_dotenv()
    #diaries_path=os.getenv("DIARIES_PATH")
    while True:
            #clear_screen()
            text1=Align("Mydiary", align="center")
            console.print(Panel(text1))
            custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # yellow + bold
])

            choice = questionary.select(
    "What would you like to manage today?",
    choices=[
        "📖 Diary Management",
        "💡 Driba Management",        
        "📁 Files Management",
        "⚙️ Profile Settings",
        "🚪 Log out"
    ],
    style=custom_style
).ask()
            if choice=="📖 Diary Management" :
                  text=Align("📖 Diary Management",align="center")
                  console.print(Panel(text))
                  from .actions import Actions
                  Actions(name)
            elif choice == "💡 Driba Management":
                  print("comming soon")
                  pass
            elif choice == "📁 Files Management":
                  print("comming soon")
                  pass
            elif choice=="⚙️ Profile Settings" :
                  print("comming soon")
                  pass
            elif choice=="🚪 Log out" :
                  text=Align("LOG OUT",align="center")
                  console.print(Panel(text))
                  console.print("Logging out...",style="bold red")
                  from .user_creation import connect
                  connect()