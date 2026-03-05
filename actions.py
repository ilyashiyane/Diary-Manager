import json
def Actions():
      try:
            with open(r"C:\Users\Lenovo\Desktop\Mydiary\diaries.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
      except FileNotFoundError:
                journal = []
      while True:
            print(20 * " " + "Commande lines" + " " * 20)
            print("1. Add a new diary")
            print("2. View all diaries")
            print("3. Search for a diary by date")
            print("4. Search for a diary by title")
            print("5. Delete a diary")
            print("6. Edit a diary")
            print("7. Exit")

            choice = input("Please select an option (1-7): ")
            if choice=="1" :
                  from add import Add
                  Add()
            elif choice == "2":
                  from view_all import ViewAll
                  ViewAll()
            elif choice == "3":
                    from search_by_date import SearchByDate
                    SearchByDate()
            elif choice == "4":
                   from search_by_title import SearchByTitle
                   SearchByTitle()
            elif choice == "5":
                    from delete import Delete
                    Delete()
            elif choice == "6":
                    from edit import Edit
                    Edit()
            elif choice == "7":
                    print("Goodbye!")
                    break

