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
        "📖 Edit a diary",
        "📂 View all diaries",
        "🔍 Search for a diary by date",
        "🔍 Search for a diary by title",
        "📤 Share a Diary",
        "🗑️ Delete a diary",
        "🏠 Go to Main Menu"
    ],
    style=custom_style
).ask()
            if choice=="📖 Add a new diary" :
                  text=Align("ADD A NEW DIARY",align="center")
                  console.print(Panel(text))
                  from .add import Add
                  Add(name)
            elif choice == "📖 Edit a diary":
                    text=Align("EDIT A DIARY",align="center")
                    console.print(Panel(text))
                    from .edit import Edit
                    Edit(name)
                    console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
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
            elif choice=="📤 Share a Diary" :
                    print("coming soon")
                    pass
            elif choice == "🗑️ Delete a diary":
                    text=Align("DELETE A DIARY",align="center")
                    console.print(Panel(text))
                    from .delete import Delete
                    Delete(name)
                    console.input(Align("Press enter to continue",align="center",style="Bold yellow"))
            elif choice == "🏠 Go to Main Menu":
                    text=Align("Main Menu",align="center")
                    console.print(Panel(text))
                    #console.print("Logging out...",style="bold red")
                    from .main_actions import main_actions
                    main_actions(name)
                    
            
                   
            

