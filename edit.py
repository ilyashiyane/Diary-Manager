import json
import os
from dotenv import load_dotenv

#try:
            #with open(f"C:/Users/Lenovo/Desktop/Mydiary/Diaries/{name}.json", "r", encoding="utf-8") as file:
                #journal = json.load(file)
#except FileNotFoundError:
                #journal = []
def Edit(name) :
                load_dotenv()
                diaries_path=os.getenv("DIARIES_PATH")
                with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                     journal = json.load(file)
                title = input("Please provide the title of the diary you want to edit. ")
                print("Choose what you want to do:")
                print("1. Edit the title")
                print("2. Edit the text")
                print("3. Edit both title and text")
                print("4. Exit")

                action = input("Enter your choice (1-4): ")

                while  action not in ["1", "2", "3","4"]:
                    print("Invalid choice. Please select 1, 2, 3, or 4.")
                    action = input("Enter your choice (1-4): ")

                if action == "1":
                    for diary in journal:
                        if diary["Title"].lower() == title.lower():
                            new_title = input("Enter the new title: ").strip()
                            diary["Title"] = new_title
                            with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                                json.dump(journal, file, indent=4, ensure_ascii=False)
                            print("The title has been edited.")
                            break

                elif action == "2":
                    lines = []
                    print("Enter the new text (type 'End' on a new line to finish):")

                    while True:
                        line = input()
                        if line.lower() == "end" or not line:
                            print("Your text is added")
                            break
                        else:
                            lines.append(line)

                    text = "\n".join(lines)

                    for diary in journal:
                        if diary["Title"].lower() == title.lower():
                            diary["Text"] = text
                            with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                                json.dump(journal, file, indent=4, ensure_ascii=False)
                            print("The text has been edited.")
                            break

                elif action == "3":
                    new_title = input("Give the new title: ").strip()
                    lines = []
                    print("Enter the new text (type 'End' on a new line to finish):")

                    while True:
                        line = input()
                        if line.lower() == "end" or not line:
                            print("Your text is added")
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
                            print("The title and the text have been edited.")
                            break
                elif action == "4":
                    print("Exiting the edit menu.")
                    from actions import Actions
                    Actions()