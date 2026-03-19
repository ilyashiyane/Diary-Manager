import json
import getpass
import os 
from dotenv import load_dotenv
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from password_criteria import password_criteria

def connect():
    console=Console()
    load_dotenv()
    diaries_path=os.getenv("DIARIES_PATH")
    users_path=os.getenv("USERSJSON_PATH")
    file_path = users_path
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []  
    if not users:
        print("There is no user. Please create the first account which is admin account.")
        name = input("Enter your name: ")
        password = getpass.getpass("Enter your password: ")
        #while not password_criteria(password) :
            #print("The password")
        password_second = getpass.getpass("Enter the second password: ")
        while password == password_second :
              console.print(Align("Passwords must not be the same . Please change the second password.",align="center",style="bold red"))
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
        console.print(Align("\nPress 1 to log in as a normal person ,or 2 to log in as admin or 0 to create a new account.",align="center",style="italic green"))
        choice = input("Your choice: ")
        if choice != "1" and choice != "2" and choice != "0":
            console.print(Align("Invalid choice. Please enter 1 to log in or 0 to create a new account.",align="center",style="bold red"))
            continue  
        if choice == "1":
            name = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password:
                    found = True
                    break
            if found:
                console.print(Align("Login successful.",align="center",style="italic green"))
                from actions import Actions
                Actions(name)
                break  
            else:
                console.print(Align("Error: Invalid credentials. Please try again.",align="center",style="bold red"))
                i += 1
                if i >= 3:
                    console.print(Align("Too many failed attempts. Exiting.",align="center",style="italic red"))
                    exit()  
            #from actions import Actions
            #Actions(name)
        elif choice == "0":  
          while True :
            name = input("Enter your name: ")
            if name=="" or len(name)<3 or len(name)>30:
                print("Username cannot be empty and must be between 3 and 30 characters long. Please enter a valid username.")
                continue
            #password = getpass.getpass("Enter your password: ")
            duplicate = False
            for user in users:
                if user["name"] == name:
                    duplicate = True
                    break
            if duplicate:
                console.print(Align("This username already exists. Try logging in or choose a different name.",align="center",style="bold red"))
                continue 
            break
          while True :
            password = getpass.getpass("Enter your password: ")
            from password_criteria import password_criteria
            if not password_criteria(password) : 
                print(Align("Password must be at least 8 characters long.",align="center",style="bold red"))
                continue
            elif password_criteria(password) :
             user = {"name": name, "password": [password]}
             users.append(user)
             with open(file_path, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
             console.print(Align("Account created successfully. Please log in again.",align="center",style="italic green"))
             with open(f"{diaries_path}/{name}.json", "x", encoding="utf-8") as file:
                json.dump([], file, indent=4, ensure_ascii=False)
             break
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
