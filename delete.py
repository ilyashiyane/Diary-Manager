import json
def Delete() :
        try:
            with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
        except FileNotFoundError:
                journal = []

        title = input("Please provide the title of the diary you want to delete.")
        for diary in journal :
            if diary["Title"].lower()==title.lower() :
                journal.remove(diary)
                with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "w", encoding="utf-8") as file:
                    json.dump(journal, file, indent=4, ensure_ascii=False)
                print("The diary has been deleted.")
                break