import json
from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import os
def Add(name) :
     console=Console()
     load_dotenv()
     diaries_path = os.getenv("DIARIES_PATH")
     try:
            with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
     except FileNotFoundError:
                journal = []

     dats = input("Please provide a date in this format: year-month-day (YYYY-MM-DD). ")
     hour = input("Please provide the current time as Hour:Minute (HH:MM). ")
     if not dats.strip() or not hour.strip():
            console.print("Enter both date and time. [bold red]Leaving either blank will default to the current date and time.")
            i = input("Press 1 for the current date and time, or 0 to enter your own date and hour. ")
            if i == "1":
                        dates = datetime.now()
            elif i == "0":
                    try:
                        dats = input("Please provide a date in this format: year-month-day (YYYY-MM-DD). ")
                        hour = input("Please provide the current time as Hour:Minute (HH:MM). ")

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
            title = input("Provide the title: ").strip()
            if not title:
                console.print(Align("The title is necessary—please insert it!",align="center",style="bold red"))

     lines = []
     while True:
        line = input()
        if line.lower() == "end" or not line:
                    console.print(Align("Your diary is added",align="center",style="italic green"))
                    break
        else:
                   lines.append(line)

     text = "\n".join(lines)

     diaries = {
                "Date": dates.isoformat(),
                "Title": title,
                "Text": text
                }

     journal.append(diaries)

     with open(f"{diaries_path}/{name}.json", "w", encoding="utf-8") as file:
                json.dump(journal, file, indent=4, ensure_ascii=False)