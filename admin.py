def Admin() :
            print(20 * " " + "Admin dashboard" + " " * 20)
            print("1. Show all users")
            print("2. Delete a user")
            print("3. Add a user")
            print("4. Log out")
            print("5. Exit")
            choice = input("Please select an option (1-4): ")
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                choice = input("Please select an option (1-4): ")
            elif choice == "1":
                    from show_users import ShowUsers
                    ShowUsers()
            elif choice == "2":
                    from delete_admin import DeleteAdmin
                    DeleteAdmin()
            elif choice == "3":
                    from add_user import AddUser
                    AddUser()
                    
            elif choice == "4":
                    print("Logging out...")
                    from user_creation import connect
                    connect()
            #elif choice == "5":
                    #print("Goodbye!")
                    #pass