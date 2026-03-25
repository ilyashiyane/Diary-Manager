import json
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.align import Align
from rich.text import Text

def Delete(name) :
        console=Console()
        load_dotenv()
        diaries_path = os.getenv("DIARIES_PATH")
        #try:
        with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
        if not journal:
                    console.print(Align("No diaries found.",align="center",style="bold red"))
                    return
        
        elif  journal:
         demand_title=Text("Please provide the title of the diary you want to delete :",style="bold yellow")  
         try :
          title = console.input(demand_title)
         except KeyboardInterrupt :
          console.print("\nReturning to main menu...", style="bold yellow")
          return 
         for diary in journal :
            if diary["Title"].lower()==title.lower() :
                journal.remove(diary)
                with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                    json.dump(journal, file, indent=4, ensure_ascii=False)
                console.print(Align("The diary has been deleted.",align="center",style="bold red"))
                break