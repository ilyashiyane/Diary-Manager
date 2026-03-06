import json
import getpass

def connect():
    
    file_path = r"C:\Users\Lenovo\Desktop\Mydiary\Users.json"

    # Try to load existing users from the JSON file
    # Problem in your code: if file is empty or corrupted, it crashes. We handle it.
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []  # No users exist yet

    # If there are no users, create the first account
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
        print("Account created successfully. Please log in.")
        # After creation, continue to login
        # Problem in your code: you used 'return', which forced user to restart
        # Solution: do not return, let them log in immediately

    # Initialize the login attempt counter outside the loop
    # Problem in your code: 'i' was inside the loop, reset each iteration
    i = 0

    # Main loop: ask user what they want to do
    while True:
        print("\nPress 1 to log in as a normal person ,or 2 to log in as admin or 0 to create a new account.")
        choice = input("Your choice: ")

        # Handle invalid choice
        if choice != "1" and choice != "2" and choice != "0":
            print("Invalid choice. Please enter 1 to log in or 0 to create a new account.")
            continue  # Go back to the top of the loop

        # Login process
        if choice == "1":
            name = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")

            # Check if a user matches the credentials
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password:
                    found = True
                    break

            if found:
                print("Login successful.")
                break  # Exit the while loop after successful login
            else:
                print("Error: Invalid credentials. Please try again.")
                i += 1
                # Limit login attempts
                if i >= 3:
                    print("Too many failed attempts. Exiting.")
                    exit()  # Stop program after 3 failed attempts

        # Account creation process
        elif choice == "0":
            name = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")

            # Optional improvement: check if name already exists
            duplicate = False
            for user in users:
                if user["name"] == name:
                    duplicate = True
                    break
            if duplicate:
                print("This username already exists. Try logging in or choose a different name.")
                continue  # Go back to the top of the loop

            user = {"name": name, "password": [password]}
            
            users.append(user)
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
            print("Account created successfully. Please log in again.")
            # Problem in your code: 'break' here made user exit instead of logging in
            # Solution: do not break, let user log in immediately
        elif choice == "2":
            name = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")
            password_second = getpass.getpass("Enter the second password: ")

            # Check if a user matches the credentials and is admin
            found = False
            for user in users:
                if user["name"] == name and user["password"][0] == password and user["password"][1] == password_second :
                    found = True
                    break

            if found:
                print("Admin login successful.")
                break  # Exit the while loop after successful login
            else:
                print("Error: Invalid credentials or not an admin. Please try again.")
                i += 1
                # Limit login attempts
                if i >= 3:
                    print("Too many failed attempts. Exiting.")
                    exit()  # Stop program after 3 failed attempts
    from actions import Actions
    Actions()
