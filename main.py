from utils import user_manager, base

manager = user_manager.UserManager()

def run():
    user_manager.game.load_scores()
    manager.load_users()
    while True:
        base.Cls()
        base.DrawLine(26)
        print("Dice Roll Game")
        print("1. Register\n2. Login\n3. Exit\n")
            
        choice = base.GetInput(3)
            
        if choice == 1:
            manager.register()
        if choice == 2:
            manager.login()
        if choice == 3:
            return



run()