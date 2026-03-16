def DeleteAdmin():
    import json
    import os
    from dotenv import load_dotenv
    load_dotenv()
    users_path=os.getenv("USERSJSON_PATH")
    file_path = users_path
    name = input("Enter the username of the user to delete: ")

    with open(file_path, "r", encoding="utf-8") as file:
        users = json.load(file)

    # Chercher l'utilisateur
    found = False
    for user in users:
        if user["name"] == name:
            users.remove(user)
            found = True
            break

    if found:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
        print(f"User '{name}' deleted successfully.")
    else:
        print("This user does not exist.")
