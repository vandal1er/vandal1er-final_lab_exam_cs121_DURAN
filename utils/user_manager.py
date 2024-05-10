from .user import *

class UserManager:
    def __init__(self):
        self.accounts = {}
    
    def load_users():
        pass

    def save_users():
        pass

    def validate_username():
        pass

    def validate_password():
        pass

    def register(self):
        while True:
            Cls()
            DrawLine(26)
            print("Account Registration\n")
            username = input("Username: ")
            if username in self.accounts:
                Pause("Username already exists.")
                continue
            if len(username) < 4 and len(username) > 0:
                Pause("Username must be at least 4 characters long.")
                continue
            if username == "":
                return
            
            pw = input("Password: ")
            if len(pw) < 8 and len(pw) > 0:
                Pause("Password must be at least 8 characters long.")
                continue
            if pw == "":
                return
            
            self.accounts[username] = User(username, pw)
            Pause("Account registration successful!")
            return
        

    def login():
        pass