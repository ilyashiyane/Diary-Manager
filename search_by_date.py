import json 
try:
            with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
except FileNotFoundError:
                journal = []
def SearchByDate() :
    dat = input("Please provide a date in this format: year-month-day (YYYY-MM-DD). ")
    for diary in journal:
                    if diary["Date"].startswith(dat):
                        print(f"Date: {diary['Date']}")
                        print(f"Title: {diary['Title']}")
                        print(f"Text: {diary['Text']}")