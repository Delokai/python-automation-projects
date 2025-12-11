import json
import os

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.filename):
            return {}
        
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_users(self):
        with open(self.filename, "w") as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, username, age):
        self.users[username] = {"age": age}
        print(f"Added user: {username}")
        self.save_users()

    def list_users(self):
        if not self.users:
            return "No users stored."
        
        result = "Users:\n"
        for username, data in self.users.items():
            result += f"- {username}, Age: {data['age']}\n"
        return result


# ---------- TEST SYSTEM ----------
manager = UserManager()

manager.add_user("David", 20)
manager.add_user("Sarah", 19)

print(manager.list_users())
