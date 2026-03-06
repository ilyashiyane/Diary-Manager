import json
def ShowUsers() :
    file_path = "C:/Users/Lenovo/Desktop/Mydiary/users.json"
    with open(file_path, "r", encoding="utf-8") as file:
        users = json.load(file)
    if not users:
        print("No users found.")
    else:
        print("List of users:")
        for user in users:
            print(f"- {user['name']}")