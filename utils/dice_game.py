from .user import *
from .score import *

class DiceGame:
    scores = []
    
    def load_scores(self):
        if not os.path.exists("data.txt"):
            with open('data.txt', 'w') as f:
                f.write("")
        else:
            with open('data.txt', 'r') as f:
                for line in f:
                    values = line.strip().split(',')
                    name = values[0]
                    score = values[1]
                    streak = values[2]
                    id = values[3]
                    
                    self.scores.append({name:Score(name, score, streak, id)})
            

    def save_scores(self):
        with open('data.txt', 'w') as f:
            try:
                for i in range(10):
                    name = list(self.scores[i].keys())[0]
                    f.write(f"{name},{self.scores[i][name].score},{self.scores[i][name].streak},{self.scores[i][name].id}\n")
            except IndexError:
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
                Cls()
                DrawLine(26)
                print(f"STAGE {stage}, ROUND {round}")
                Loading(f"{user.name} is rolling the die")
                playerRoll = random.randint(1, 6)
                #playerRoll = 6 rig
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
                Pause("Press Enter to continue.")
                Cls()
                if playerScore >= 3 or cpuScore >= 3:
                    break
            breakLoop = False
            continueLoop = True
            if playerScore > cpuScore:
                gameScore += 3
                stagesWon += 1
                
                while True:
                    Cls()
                    DrawLine(26)
                    print(f"Score: {gameScore}\nNext Stage: {stage+1}\n")
                    
                    print("Stage won! Keep playing?")
                    choice = GetInput(1, 0, "Enter 0 to quit, 1 to keep playing: ")
                    
                    if choice == "error":
                        breakLoop = True
                        continue
                    
                    if choice == 1:
                        round = 1
                        stage += 1
                        cpuScore = 0
                        playerScore = 0
                        breakLoop = True
                        break
                    elif choice == 0:
                        breakLoop = False
                        continueLoop = False
                        break
            if breakLoop: continue
            
            Cls()
            DrawLine(26)
            print("Game over!\n")
            print(f"Stages won: {stagesWon}")
            print(f"Score: {gameScore}")
            DrawLine(26)
            if stagesWon > 0:
                gameID = user.name + str(gameScore) + datetime.datetime.now().strftime("%Y%m%d%H%M")
                self.scores.append({user.name:Score(user.name, gameScore, stagesWon, gameID)})
                self.scores = sorted(self.scores,key=GetScore,reverse=True)
                self.save_scores()
            #this isnt working yet
            Pause()
            if continueLoop: break
            return
            
            
            
                


    def show_top_scores(self):
        Cls()
        DrawLine(26)
        print("LEADERBOARDS\n")
        for i in range(len(self.scores)):
            if i > 9: break
            name = list(self.scores[i].keys())[0]
            score = self.scores[i][name].score
            streak = self.scores[i][name].streak
            
            print(f"{i+1}. {name}    Score: {score}    Win Streak: {streak}")
            
        Pause()

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
                self.show_top_scores()
            if choice == 3:
                return
            
        
        
