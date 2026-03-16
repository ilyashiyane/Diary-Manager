import json
import os
from dotenv import load_dotenv
def ShowUsers() :
    load_dotenv()
    users_path=os.getenv("USERSJSON_PATH")
    file_path = users_path
    with open(file_path, "r", encoding="utf-8") as file:
        users = json.load(file)
    if not users:
        print("No users found.")
    else:
        print("List of users:")
        for user in users:
            print(f"- {user['name']}")