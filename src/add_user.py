def AddUser() :
    import json
    import getpass
    import os
    from dotenv import load_dotenv
    from rich.text import Text
    from rich.console import Console
    from rich.align import Align
    load_dotenv()
    console=Console()
    diaries_path = os.getenv("DIARIES_PATH")
    users_path=os.getenv("USERSJSON_PATH")
    file_path=users_path
    with open(file_path, "r", encoding="utf-8") as file:
        users = json.load(file)
    
    while True :
     demande_name=Text("Enter the new user's name: ",style="bold yellow")
     try :
            name = console.input(demande_name)
     except KeyboardInterrupt :
            console.print("\nReturning to main menu...", style="bold yellow")
            return
     if name=="" or len(name)<3 or len(name)>30 :
           console.print(Align("Username cannot be empty and must be between 3 and 30 characters long. Please enter a valid username.",align="center",style="bold red")) 
           continue
     duplicate = False
     for user in users:
            if user["name"] == name:
                duplicate = True
                break
     if duplicate:
            print("This username already exists. Try logging in or choose a different name.")
            continue
     else :
          break
    while True :
      try :
            demande_password=Text("Enter your password: ",style="bold yellow")
            console.print(demande_password,end="")
            password = getpass.getpass("")
      except KeyboardInterrupt :
            console.print("\nReturning to main menu...", style="bold yellow")
            break
      from .password_criteria import password_criteria
      if not password_criteria(password) :
           console.print(Align("Password must be at least 8 characters long.",align="center",style="bold red"))
           continue
      else :
           break
              
    user = {"name": name, "password": [password]}
    users.append(user)
    with open(file_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
    print("Account created successfully. Please log in again.")
    with open(f"{diaries_path}/{name}.json", "x", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)
     #break