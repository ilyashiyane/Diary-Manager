import json
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
def Edit(name) :
                console=Console()
                load_dotenv()
                diaries_path=os.getenv("DIARIES_PATH")
                with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                     journal = json.load(file)
                title = input("Please provide the title of the diary you want to edit. ")
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
                print("1. Edit the title")
                print("2. Edit the text")
                print("3. Edit both title and text")
                print("4. Exit")

                action = input("Enter your choice (1-4): ")

                while  action not in ["1", "2", "3","4"]:
                    action=input("Invalid choice. Please select 1, 2, 3, or 4.")
                    

                if action == "1":
                    for diary in journal:
                        if diary["Title"].lower() == title.lower():
                            new_title = input("Enter the new title: ").strip()
                            diary["Title"] = new_title
                            with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                                json.dump(journal, file, indent=4, ensure_ascii=False)
                            console.print(Align("The title has been edited.",align="center",style="italic green"))
                            break
                elif action == "2":
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

                elif action == "3":
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
                elif action == "4":
                    console.print(Align("Exiting the edit menu.",align="center",style="bold red"))
                    from actions import Actions
                    Actions(name)