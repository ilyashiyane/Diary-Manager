import json
def ViewAll(name):
    try:
            with open(f"C:/Users/Lenovo/Desktop/Mydiary/Diaries/{name}.json", "r", encoding="utf-8") as file:
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