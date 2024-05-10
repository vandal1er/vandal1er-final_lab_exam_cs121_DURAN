from utils import dice_game,user_manager, base


game = dice_game.DiceGame()
manager = user_manager.UserManager()

def run():
    while True:
        base.Cls()
        base.DrawLine(26)
        print("Welcome to Dice Roll Game!")
        print("1. Register\n2. Login\n3. Exit")
            
        choice = base.GetInput(3)
            
        if choice == 1:
            manager.register()
    
run()