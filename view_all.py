import json
def ViewAll() :
    try:
            with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
    except FileNotFoundError:
                print("No diaries found.")
    if not journal:
                    print("No diaries found.")
    else:
            for diary in journal:
                print(f"Date: {diary['Date']}")
                print(f"Title: {diary['Title']}")
                print(f"Text: {diary['Text']}")