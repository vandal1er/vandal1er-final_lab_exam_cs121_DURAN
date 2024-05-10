def Pause(message=""):
    input(message)

def GetInput(max, min=1,message="Enter choice: "):
    try:
        choice = int(input(message))
        
        if choice > max or choice < min:
            raise ValueError
        
        return choice
    except ValueError:
        Pause("Invalid input. Please try again.")
        
