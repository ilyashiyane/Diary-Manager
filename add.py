import json
from datetime import datetime
def Add() :
     try:
            with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
     except FileNotFoundError:
                journal = []

     dats = input("Please provide a date in this format: year-month-day (YYYY-MM-DD). ")
     hour = input("Please provide the current time as Hour:Minute (HH:MM). ")
     if not dats.strip() or not hour.strip():
            print("Enter both date and time. Leaving either blank will default to the current date and time.")
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
                        print("The current date will be used")
                        dates = datetime.now()
     elif  dats.strip() or  hour.strip():
          date_format = datetime.strptime(dats, "%Y-%m-%d").date()
          time_format = datetime.strptime(hour, "%H:%M").time()
          dates = datetime.combine(date_format, time_format)

     title = ""
     while not title:
            title = input("Provide the title: ").strip()
            if not title:
                print("The title is necessary—please insert it!")

     lines = []
     while True:
        line = input()
        if line.lower() == "end" or not line:
                    print("Your text is added")
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

     with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "w", encoding="utf-8") as file:
                json.dump(journal, file, indent=4, ensure_ascii=False)