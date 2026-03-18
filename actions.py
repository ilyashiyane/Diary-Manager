import json
import os
from dotenv import load_dotenv
from rich.console import Console 
from rich.panel import Panel
from rich.align import Align

def Actions(name):
      console = Console()
      load_dotenv()
      diaries_path=os.getenv("DIARIES_PATH")
      try:
            with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
      except FileNotFoundError:
                journal = []
      while True:
            text1=Align("Mydiary", align="center")
            console.print(Panel(text1))
            print("1. Add a new diary")
            print("2. View all diaries")
            print("3. Search for a diary by date")
            print("4. Search for a diary by title")
            print("5. Delete a diary")
            print("6. Edit a diary")
            print("7. Settings")
            print("8. Log out")
            
            choice = input("Please select an option (1-8): ")
            if choice=="1" :
                  text=Align("ADD A NEW DIARY",align="center")
                  console.print(Panel(text))
                  from add import Add
                  Add(name)
            elif choice == "2":
                  text=Align("View ALL DIARIES",align="center")
                  console.print(Panel(text))
                  from view_all import ViewAll
                  ViewAll(name)
            elif choice == "3":
                    text=Align("SEARCH A DIARY BY DATE",align="center")
                    console.print(Panel(text))
                    from search_by_date import SearchByDate
                    SearchByDate(name)
            elif choice == "4":
                   text=Align("SEARCH A DIARY BY TITLE",align="center")
                   console.print(Panel(text))
                   from search_by_title import SearchByTitle
                   SearchByTitle(name)
            elif choice == "5":
                    text=Align("DELETE A DIARY",align="center")
                    console.print(Panel(text))
                    from delete import Delete
                    Delete(name)
            elif choice == "6":
                    text=Align("EDIT A DIARY",align="center")
                    console.print(Panel(text))
                    from edit import Edit
                    Edit(name)
            elif choice == "7":
                   pass
            elif choice == "8":
                    text=Align("LOG OUT",align="center")
                    console.print(Panel(text))
                    print("Logging out...")
                    from user_creation import connect
                    connect()
            else :
                   console.print("[bold red]Error ! Please chose a number between 0 and 8")
                   continue
            

