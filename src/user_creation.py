import json
import getpass
import os 
import questionary
import sys
import bcrypt
from rich.text import Text
from dotenv import load_dotenv
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from .password_criteria import password_criteria
import hashlib
from questionary import Style
def connect():
    #def clear_screen():
                #os.system('cls' if os.name == 'nt' else 'clear')
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
        password_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        password_hash_second=bcrypt.hashpw(password_second.encode(),bcrypt.gensalt()).decode()
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
    "Choose an option:(press control c in order to go back while putting inputs)",
    choices=[
        "🆕 Create a new account",
        "👤 Log in as a normal user",
        "🛡️ Log in as admin",
        "🚪 Exit the application"
    ],
    style=custom_style
).ask()  
        if choice == "👤 Log in as a normal user":
            
            if len(users)==1 :
                console.print(Align("There is no user please create one first by pressing 0",align="center",style="bold red"))
                continue
            demande_name=Text("Enter your name: ", style="bold yellow")
            try :
                name = console.input(demande_name)
            except KeyboardInterrupt :
                 console.print("\nReturning to main menu...", style="bold yellow")
                 continue
            
            demande_password=Text("Enter your password: ",style="bold yellow")
            try :
               console.print(demande_password, end="")
               password = getpass.getpass("")
            except KeyboardInterrupt :
               console.print("\nReturning to main menu...", style="bold yellow")
               continue
            found = False
            for user in users:
                if user["name"] == name and bcrypt.checkpw(password.encode(),user["password"][0].encode()):
                    found = True
                    break
            if found:
                console.print(Align("Login successful.",align="center",style="italic green"))
                from .main_actions import main_actions
                main_actions(name)
                break  
            else:
                console.print(Align("Error: Invalid credentials. Please try again.",align="center",style="bold red"))
                console.input(Align("press enter to continue",align="center",style="bold yellow"))
                i += 1
                if i >= 3:
                    console.print(Align("Too many failed attempts. Exiting.",align="center",style="bold red"))
                    exit()  
            
        elif choice == "🆕 Create a new account":  
         try :
          while True :
            demande_name=Text("Enter your name: ",style="bold yellow")
            try:
             name = console.input(demande_name)
            except KeyboardInterrupt:
             console.print("\nReturning to main menu...", style="bold yellow")
             name = None
             break 
            if name=="" or len(name)<3 or len(name)>30 :
                console.print(Align("Username cannot be empty and must be between 3 and 30 characters long. Please enter a valid username.",align="center",style="bold red"))
                continue
            elif not name.isalnum() :
                console.print(Align("Username must be only in alphabetics and numeric.Please enter a valid username.",align="center",style="bold red"))
                continue
            duplicate = False
            for user in users:
                if user["name"] == name:
                    duplicate = True
                    break
            if duplicate:
                console.print(Align("This username already exists. Try logging in or choose a different name.",align="center",style="bold red"))
                continue 
            
            while True :
             demande_password=Text("Enter your password: ",style="bold yellow")
             console.print(demande_password,end="")
             password = getpass.getpass("")
             from .password_criteria import password_criteria
             if not password_criteria(password) : 
                console.print(Align("Password must be at least 8 characters long.",align="center",style="bold red"))
                continue
             elif password_criteria(password) :
              password_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
              user = {"name": name, "password": [password_hash]}
              users.append(user)
              with open(file_path, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
              console.print(Align("Account created successfully. Please log in again.",align="center",style="italic green"))
              with open(f"{diaries_path}/{name}.json", "x", encoding="utf-8") as file:
                json.dump([], file, indent=4, ensure_ascii=False)
              break
            break
         except KeyboardInterrupt:
           console.print("\nReturning to main menu...", style="bold yellow")
           name = None
         if name is not None:
           from .main_actions import main_actions
           main_actions(name)
        elif choice == "🛡️ Log in as admin":
            demande_name=Text("Enter your name: ",style="bold yellow")
            try :
                name = console.input(demande_name)
            except KeyboardInterrupt :
                 console.print("\nReturning to main menu...", style="bold yellow")
                 continue
            demande_password=Text("Enter your password: ",style="bold yellow")
            console.print(demande_password,end="")
            try :
                password = getpass.getpass("")
            except KeyboardInterrupt :
                console.print("\nReturning to main menu...", style="bold yellow")
                continue
            demande_password_second=Text("Enter your second password: ",style="bold yellow")
            console.print(demande_password_second,end="")
            try :
                password_second = getpass.getpass("")
            except :
                console.print("\nReturning to main menu...", style="bold yellow")
                continue
            found = False
            for user in users:
                if user["name"] == name and bcrypt.checkpw(password.encode(),user["password"][0].encode()) and bcrypt.checkpw(password_second.encode(),user["password"][1].encode()) :
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
        elif choice=="🚪 Exit the application" :
            console.print("Logging out... ",style="bold red")
            sys.exit()
    
    
