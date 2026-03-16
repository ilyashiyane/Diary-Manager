import json
from dotenv import load_dotenv
import os

def Delete(name) :
        load_dotenv()
        diaries_path = os.getenv("DIARIES_PATH")
        #try:
        with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
        if not journal:
                    print("No diaries found.")
                    return
        #except FileNotFoundError:
                #journal = []
        elif  journal:
                    
         title = input("Please provide the title of the diary you want to delete.")
         for diary in journal :
            if diary["Title"].lower()==title.lower() :
                journal.remove(diary)
                with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                    json.dump(journal, file, indent=4, ensure_ascii=False)
                print("The diary has been deleted.")
                break