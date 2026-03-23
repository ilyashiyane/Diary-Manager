import json
import os
import questionary
from dotenv import load_dotenv
from rich.console import Console 
from rich.panel import Panel
from rich.align import Align
from questionary import Style
def Actions(name):
      def clear_screen():
         os.system('cls' if os.name == 'nt' else 'clear')
      console = Console()
      load_dotenv()
      diaries_path=os.getenv("DIARIES_PATH")
      try:
            with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
      except FileNotFoundError:
                journal = []
      while True:
            clear_screen()
            text1=Align("Mydiary", align="center")
            console.print(Panel(text1))
            custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # jaune + bold
])
            choice = questionary.select(
    "What would you like to do today?",
    choices=[
        "📖 Add a new diary",
        "📂 View all diaries",
        "🔍 Search for a diary by date",
        "🔍 Search for a diary by title",
        "📖 Edit a diary",
        "🗑️ Delete a diary",
        "⚙️ Settings",
        "🚪 Log out"
    ],
    style=custom_style
).ask()
            if choice=="📖 Add a new diary" :
                  text=Align("ADD A NEW DIARY",align="center")
                  console.print(Panel(text))
                  from .add import Add
                  Add(name)
                  console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "📂 View all diaries":
                  text=Align("View ALL DIARIES",align="center")
                  console.print(Panel(text))
                  from .view_all import ViewAll
                  ViewAll(name)
                  console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "🔍 Search for a diary by date":
                    text=Align("SEARCH A DIARY BY DATE",align="center")
                    console.print(Panel(text))
                    from .search_by_date import SearchByDate
                    SearchByDate(name)
                    console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "🔍 Search for a diary by title":
                   text=Align("SEARCH A DIARY BY TITLE",align="center")
                   console.print(Panel(text))
                   from .search_by_title import SearchByTitle
                   SearchByTitle(name)
                   console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "🗑️ Delete a diary":
                    text=Align("DELETE A DIARY",align="center")
                    console.print(Panel(text))
                    from .delete import Delete
                    Delete(name)
                    console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "📖 Edit a diary":
                    text=Align("EDIT A DIARY",align="center")
                    console.print(Panel(text))
                    from .edit import Edit
                    Edit(name)
                    console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "⚙️ Settings":
                   pass
            elif choice == "🚪 Log out":
                    text=Align("LOG OUT",align="center")
                    console.print(Panel(text))
                    console.print("Logging out...",style="bold red")
                    from .user_creation import connect
                    connect()
                    
            
                   
            

