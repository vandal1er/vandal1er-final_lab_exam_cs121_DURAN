from utils import dice_game,user_manager, base, user



manager = user_manager.UserManager()

def run():
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

user_manager.game.play_game(user.User("Jasiel", "James"))
run()