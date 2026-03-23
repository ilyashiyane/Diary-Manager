import json
import os
import questionary
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from questionary import Style
def Edit(name) :
                console=Console()
                load_dotenv()
                diaries_path=os.getenv("DIARIES_PATH")
                with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                     journal = json.load(file)
                demande_title=Text("Please provide the title of the diary you want to edit : ",style="bold yellow")
                title = console.input(demande_title)
                found=False
                for diaries in journal :
                     if diaries["Title"]==title :
                          found=True
                          break
                while not found :
                 console.print(Align("No such diary with this title try another title",align="center",style="bold red"))
                 title = input("Please provide the title of the diary you want to edit. ")
                 for diaries in journal :
                     if diaries["Title"]==title :
                          found=True
                          break
                     
                console.print(Align("Choose what you want to do:",align="center",style="italic green"))
                custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # jaune + bold
])
                choice = questionary.select(
    "What would you like to edit?",
    choices=[
        "✏️ Edit the title",
        "📝 Edit the text",
        "🖋️ Edit both title and text",
        "🚪 Exit"
    ],
    style=custom_style
).ask()
                
                    

                if choice == "✏️ Edit the title":
                    for diary in journal:
                        if diary["Title"].lower() == title.lower():
                            new_title = input("Enter the new title: ").strip()
                            diary["Title"] = new_title
                            with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                                json.dump(journal, file, indent=4, ensure_ascii=False)
                            console.print(Align("The title has been edited.",align="center",style="italic green"))
                            break
                elif choice == "📝 Edit the text":
                    lines = []
                    console.print(Align("Enter the new text (type 'End' on a new line to finish):",align="center",style="italic green"))
                    while True:
                        line = input()
                        if line.lower() == "end" or not line:
                            console.print(Align("Your text is added",align="center",style="italic green"))
                            break
                        else:
                            lines.append(line)

                    text = "\n".join(lines)

                    for diary in journal:
                        if diary["Title"].lower() == title.lower():
                            diary["Text"] = text
                            with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                                json.dump(journal, file, indent=4, ensure_ascii=False)
                            console.print(Align("The text has been edited.",align="center",style="italic green"))
                            break

                elif choice == "🖋️ Edit both title and text":
                    new_title = input("Give the new title: ").strip()
                    lines = []
                    console.print(Align("Enter the new text (type 'End' on a new line to finish):",align="center",style="italic green"))

                    while True:
                        line = input()
                        if line.lower() == "end" or not line:
                            console.print(Align("Your text is added",align="center",style="italic green"))
                            break
                        else:
                            lines.append(line)

                    text = "\n".join(lines)

                    for diary in journal:
                        if diary["Title"].lower() == title.lower():
                            diary["Title"] = new_title
                            diary["Text"] = text
                            with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                                json.dump(journal, file, indent=4, ensure_ascii=False)
                            console.print(Align("The title and the text have been edited.",align="center",style="italic green"))
                            
                            break
                elif choice == "🚪 Exit":
                    console.print(Align("Exiting the edit menu.",align="center",style="bold red"))
                    from actions import Actions
                    Actions(name)