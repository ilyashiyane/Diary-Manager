import json
def Actions(name):
      try:
            with open(f"C:/Users/Lenovo/Desktop/Mydiary/Diaries/{name}.json", "r", encoding="utf-8") as file:
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
            print("7. log out")
            #print("8. Exit")

            choice = input("Please select an option (1-7): ")
            if choice=="1" :
                  from add import Add
                  Add(name)
            elif choice == "2":
                  from view_all import ViewAll
                  ViewAll(name)
            elif choice == "3":
                    from search_by_date import SearchByDate
                    SearchByDate(name)
            elif choice == "4":
                   from search_by_title import SearchByTitle
                   SearchByTitle(name)
            elif choice == "5":
                    from delete import Delete
                    Delete(name)
            elif choice == "6":
                    from edit import Edit
                    Edit(name)
            elif choice == "7":
                    print("Logging out...")
                    from user_creation import connect
                    connect()
            #elif choice == "8":
                    #print("Goodbye!")
                    #break

