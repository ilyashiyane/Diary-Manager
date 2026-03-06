import json 
#try:
            #with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "r", encoding="utf-8") as file:
                #journal = json.load(file)
#except FileNotFoundError:
                #journal = []
def SearchByTitle(name) :
        with open(f"C:/Users/Lenovo/Desktop/Mydiary/Diaries/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
        title = input("Please provide the title of the diary you want to search for. ")
        for diary in journal:
                    if diary["Title"].lower() == title.lower():
                        print(f"Date: {diary['Date']}")
                        print(f"Title: {diary['Title']}")
                        print(f"Text: {diary['Text']}")