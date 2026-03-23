import json
import getpass
import os 
import questionary
import sys
from rich.text import Text
from dotenv import load_dotenv
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from .password_criteria import password_criteria
import hashlib
from questionary import Style
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
        console.print(Align("There is no user. Please create the first account which is admin account.",align="center",style="italic green"))
        demande_name=Text("Enter your name: ",style="bold yellow")
        name = console.input(demande_name)
        password = getpass.getpass("Enter your password: ")
        
        password_second = getpass.getpass("Enter the second password: ")
        while password == password_second :
              console.print(Align("Passwords must not be the same . Please change the second password.",align="center",style="bold red"))
              password_second = getpass.getpass("Enter the second password again : ")
              if password != password_second :
                    console.print(Align("Passwords are different. Account created successfully.",align="center",style="italic green"))
                    break
        password_hash=hashlib.sha256(password.encode()).hexdigest()
        password_hash_second=hashlib.sha256(password_second.encode()).hexdigest()
        user = {"name": name, "password": [password_hash, password_hash_second]}
        users.append(user)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
        console.print(Align("Admin account created successfully. Please log in.",align="center",style="italic green"))
    i = 0
    while True:
        custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # jaune + bold
])
        choice = questionary.select(
    "Choose an option:",
    choices=[
        "🆕 Create a new account",
        "👤 Log in as a normal user",
        "🛡️ Log in as admin",
        "🚪 Log out"
    ],
    style=custom_style
).ask()  
        if choice == "👤 Log in as a normal user":
            if len(users)==1 :
                console.print(Align("There is no user please create one first by pressing 0",align="center",style="bold red"))
                continue
            demande_name=Text("Enter your name: ", style="bold yellow")
            name = console.input(demande_name)
            demande_password=Text("Enter your password: ",style="bold yellow")
            console.print(demande_password, end="")
            password = getpass.getpass("")
            password_hash=hashlib.sha256(password.encode()).hexdigest()
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password_hash:
                    found = True
                    break
            if found:
                console.print(Align("Login successful.",align="center",style="italic green"))
                from .actions import Actions
                Actions(name)
                break  
            else:
                console.print(Align("Error: Invalid credentials. Please try again.",align="center",style="bold red"))
                console.input(Align("press enter to continue",align="center",style="bold yellow"))
                i += 1
                if i >= 3:
                    console.print(Align("Too many failed attempts. Exiting.",align="center",style="bold red"))
                    exit()  
        elif choice == "🆕 Create a new account":  
          while True :
            demande_name=Text("Enter your name: ",style="bold yellow")
            name = console.input(demande_name)
            if name=="" or len(name)<3 or len(name)>30:
                console.print(Align("Username cannot be empty and must be between 3 and 30 characters long. Please enter a valid username.",align="center",style="bold red"))
                continue
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
            demande_password=Text("Enter your password: ",style="bold yellow")
            console.print(demande_password,end="")
            password = getpass.getpass("")
            from password_criteria import password_criteria
            if not password_criteria(password) : 
                console.print(Align("Password must be at least 8 characters long.",align="center",style="bold red"))
                continue
            elif password_criteria(password) :
             password_hash=hashlib.sha256(password.encode()).hexdigest()
             user = {"name": name, "password": [password_hash]}
             users.append(user)
             with open(file_path, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
             console.print(Align("Account created successfully. Please log in again.",align="center",style="italic green"))
             with open(f"{diaries_path}/{name}.json", "x", encoding="utf-8") as file:
                json.dump([], file, indent=4, ensure_ascii=False)
             break
          from .actions import Actions
          Actions(name)
        elif choice == "🛡️ Log in as admin":
            demande_name=Text("Enter your name: ",style="bold yellow")
            name = console.input(demande_name)
            demande_password=Text("Enter your password: ",style="bold yellow")
            console.print(demande_password,end="")
            password = getpass.getpass("")
            password_hash=hashlib.sha256(password.encode()).hexdigest()
            demande_password_second=Text("Enter your second password: ",style="bold yellow")
            console.print(demande_password_second,end="")
            password_second = getpass.getpass("")
            password_second_hash=hashlib.sha256(password_second.encode()).hexdigest()
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password_hash and user["password"][1] == password_second_hash :
                    found = True
                    break
            if found:
                console.print(Align("Admin login successful.",align="center",style="italic green"))
                from .admin import Admin
                Admin()
                break  
            else:
                console.print(Align("Error: Invalid credentials or not an admin. Please try again.",align="center",style="bold red"))
                console.input(Align("press enter to continue",align="center",style="bold yellow"))
                i += 1
                if i >= 3:
                    console.print(Align("Too many failed attempts. Exiting.",align="center",style="bold red"))
                    exit()  
        elif choice=="🚪 Log out" :
            console.print("Logging out... ",style="bold red")
            sys.exit()
    
    
