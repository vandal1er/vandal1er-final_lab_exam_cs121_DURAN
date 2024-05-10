from .user import *

class DiceGame:
    def load_scores():
        pass

    def save_scores():
        pass

    def play_game(self, user):
        stage = 1
        round = 1
        gameScore = 0
        playerScore = 0
        cpuScore = 0
        stagesWon = 0
        while True:
            while True:
                DrawLine(26)
                print(f"STAGE {stage}, ROUND {round}")
                Loading(f"{user.name} is rolling the die")
                playerRoll = random.randint(1, 6)
                print(f"\n{user.name} rolled a {playerRoll}!\n")
                time.sleep(0.5)
                Loading("CPU is rolling the die")
                cpuRoll = random.randint(1, 6)
                print(f"\nCPU rolled a {cpuRoll}!")
                time.sleep(0.5)
                
                if playerRoll > cpuRoll:
                    print(f"\n{user.name} wins this round!")
                    playerScore += 1
                    gameScore+=1
                    
                elif playerRoll < cpuRoll:
                    print(f"\nCPU wins this round!")
                    cpuScore += 1
                else:
                    print(f"\nIt's a tie!")
                    
                round += 1
                Pause("")
                Cls()
                if playerScore + cpuScore >= 3:
                    break
            
            if playerScore > cpuScore:
                gameScore += 3
                stagesWon += 1
                DrawLine(26)
                print(f"Score: {gameScore}\nNext Stage: {stage+1}\n")
                
                print("Stage won! Keep playing?")
                choice = GetInput(1, 0, "Enter 0 to quit, 1 to keep playing: ")
                
                if choice == 1:
                    round = 0
                    stage += 1
                    cpuScore = 0
                    playerScore = 0
                    continue
                
            
                


    def show_top_scores():
        pass

    def logout():
        pass

    def menu(self, user):
        while True:
            Cls()
            DrawLine(26)
            print(f"Welcome, {user.name}")
            print("1. Start Game\n2. Leaderboards\n3. Log Out\n")
            
            choice = GetInput(3)
            
            if choice == 1:
                self.play_game(user)
            if choice == 2:
                pass
            
        
        
