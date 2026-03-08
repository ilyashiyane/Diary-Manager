import json
import getpass

def connect():
    file_path = r"C:\Users\Lenovo\Desktop\Mydiary\Users.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []  
    if not users:
        print("There is no user. Please create the first account which is admin account.")
        name = input("Enter your name: ")
        password = getpass.getpass("Enter your password: ")
        password_second = getpass.getpass("Enter the second password: ")
        while password == password_second :
              print("Passwords must not be the same . Please change the second password.")
              password_second = getpass.getpass("Enter the second password again : ")
              if password != password_second :
                    print("Passwords are different. Account created successfully.")
                    break
        user = {"name": name, "password": [password, password_second]}
        users.append(user)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
        print("Admin account created successfully. Please log in.") 
    i = 0
    while True:
        print("\nPress 1 to log in as a normal person ,or 2 to log in as admin or 0 to create a new account.")
        choice = input("Your choice: ")
        if choice != "1" and choice != "2" and choice != "0":
            print("Invalid choice. Please enter 1 to log in or 0 to create a new account.")
            continue  
        if choice == "1":
            from brute_force import brute_force
            name = input("Enter your name: ")
            password,time,tries = brute_force(name)  #getpass.getpass("Enter your password: ")
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password:
                    found = True
                    break
            if found:
                print("Login successful.")
                print(f"Time taken to brute-force the password: {time:.2f} seconds")
                print(f"Number of attempts: {tries}")
                from actions import Actions
                Actions(name)
                break  
            else:
                print("Error: Invalid credentials. Please try again.")
                #i += 1
                #if i >= 3:
                    #print("Too many failed attempts. Exiting.")
                    #exit()  
            #from actions import Actions
            #Actions(name)
        elif choice == "0":
            name = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")
            duplicate = False
            for user in users:
                if user["name"] == name:
                    duplicate = True
                    break
            if duplicate:
                print("This username already exists. Try logging in or choose a different name.")
                continue  
            user = {"name": name, "password": [password]}
            users.append(user)
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
            print("Account created successfully. Please log in again.")
            with open(f"C:/Users/Lenovo/Desktop/Mydiary/Diaries/{name}.json", "x", encoding="utf-8") as file:
                json.dump([], file, indent=4, ensure_ascii=False)
            from actions import Actions
            Actions(name)
        elif choice == "2":
            name = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")
            password_second = getpass.getpass("Enter the second password: ")
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password and user["password"][1] == password_second :
                    found = True
                    break
            if found:
                print("Admin login successful.")
                from admin import Admin
                Admin()
                break  
            else:
                print("Error: Invalid credentials or not an admin. Please try again.")
                i += 1
                if i >= 3:
                    print("Too many failed attempts. Exiting.")
                    exit()  
    #from actions import Actions
    #Actions(name)
