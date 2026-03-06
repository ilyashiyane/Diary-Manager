def AddUser() :
    import json
    import getpass
    file_path="C:/Users/Lenovo/Desktop/Mydiary/users.json"
    with open(file_path, "r", encoding="utf-8") as file:
        users = json.load(file)
    
    while True :
     name = input("Enter the new user's name: ")
     password = getpass.getpass("Enter the new user's password: ")
     duplicate = False
     for user in users:
            if user["name"] == name:
                duplicate = True
                #print("This username already exists. Choose a different name.")
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
     break