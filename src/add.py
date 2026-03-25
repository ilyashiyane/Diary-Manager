import json
import questionary
from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import os
from questionary import Style
import subprocess
def Add(name) :
     console=Console()
     load_dotenv()
     diaries_path = os.getenv("DIARIES_PATH")
     try:
            with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
     except FileNotFoundError:
                journal = []
     demande_dats=Text("Please provide a date in this format: year-month-day (YYYY-MM-DD) :",style="bold yellow")
     try :
            dats = console.input(demande_dats)
     except KeyboardInterrupt :
            console.print("\nReturning to main menu...", style="bold yellow")
            return
            
     #demande_dats=Text("Please provide a date in this format: year-month-day (YYYY-MM-DD) :",style="bold yellow")
     #dats = console.input(demande_dats)
     demande_hour=Text("Please provide the current time as Hour:Minute (HH:MM) :",style="bold yellow")
     try:
         hour = console.input(demande_hour)
     except KeyboardInterrupt :
            console.print("\nReturning to main menu...", style="bold yellow")
            return
     if not dats.strip() or not hour.strip():
            console.print("[bold red] Enter both date and time. Leaving either blank will default to the current date and time.")
            custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # jaune + bold
])
            choice = questionary.select(
    "What do you want?",
    choices=[
        "Current date and time",
        "Enter your own date and hour"
    ],
    style=custom_style
).ask()
            if choice == "Current date and time":
                        dates = datetime.now()
            elif choice == "Enter your own date and hour":
                    try:
                        demande_dats=Text("Please provide a date in this format: year-month-day (YYYY-MM-DD) : ",style="bold yellow")
                        dats = console.input(demande_dats)
                        demande_hour=Text("Please provide the current time as Hour:Minute (HH:MM) :",style="bold yellow")
                        hour = console.input(demande_hour)
                        date_format = datetime.strptime(dats, "%Y-%m-%d").date()
                        time_format = datetime.strptime(hour, "%H:%M").time()
                        dates = datetime.combine(date_format, time_format)
                    except ValueError:
                        console.print(Align("The current date will be used",align="center",style="bold red"))
                        dates = datetime.now()
     elif  dats.strip() or  hour.strip():
          date_format = datetime.strptime(dats, "%Y-%m-%d").date()
          time_format = datetime.strptime(hour, "%H:%M").time()
          dates = datetime.combine(date_format, time_format)

     title = ""
     while not title:
            demande_title=Text("Provide the title: ",style="bold yellow")
            try :
             title = console.input(demande_title).strip()
            except KeyboardInterrupt :
             console.print("\nReturning to main menu...", style="bold yellow")
             return
            if not title:
                console.print(Align("The title is necessary—please insert it!",align="center",style="bold red"))

     lines = []
     console.print(Align("Write you diary here",align="center",style="italic green"))
     console.print(Align("A text editor (Notepad) will open. Write your journal, save it (Ctrl+S), and close the window.", align="center", style="italic green"))
     
     # 1. Nom du fichier temporaire invisible
     temp_file = "temp_diary.txt"
     
     # 2. Création d'un fichier vide pour l'éditeur
     with open(temp_file, "w", encoding="utf-8") as file:
         file.write("")
         
     # 3. Ouverture du Bloc-Notes et PAUSE du script Python jusqu'à la fermeture
     subprocess.run(["notepad", temp_file])
     
     # 4. Quand l'utilisateur ferme Notepad, Python se réveille et lit le fichier
     with open(temp_file, "r", encoding="utf-8") as file:
         text = file.read().strip() # .strip() enlève les espaces vides au début/fin
         
     # 5. On supprime le fichier temporaire pour ne laisser aucune trace 
     # (Très important pour la confidentialité !)
     if os.path.exists(temp_file):
         os.remove(temp_file)
         
     # 6. Vérification au cas où l'utilisateur n'a rien écrit du tout
     if not text:
         console.print(Align("Addition canceled: You didn’t write anything in Notepad.", align="center", style="bold red"))
         return
         
     console.print(Align("Your diary is added", align="center", style="italic green"))


     diaries = {
                "Date": dates.isoformat(),
                "Title": title,
                "Text": text
                }

     journal.append(diaries)

     with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                json.dump(journal, file, indent=4, ensure_ascii=False)