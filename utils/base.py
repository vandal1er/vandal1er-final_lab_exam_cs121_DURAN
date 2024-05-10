import os

def Pause(message=""):
    input(message)

def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def GetInput(max, min=1,message="Enter choice: "):
    try:
        choice = int(input(message))
        
        if choice > max or choice < min:
            raise ValueError
        
        return choice
    except ValueError:
        Pause("Invalid input. Please try again.")
        
def DrawLine(length=10):
    for i in range(length):
        print("_", end="")
    print("")