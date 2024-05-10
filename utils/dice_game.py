from base import *

class DiceGame:
    '''def load_scores():
        pass

	def save_scores():
		pass

	def play_game():
		pass

	def show_top_scores():
		pass

	def logout():
		pass'''

    def menu():
        DrawLine()
        print("Welcome to Dice Roll Game!")
        print("1. Register\n2.Login\n3.Exit")
        
        choice = GetInput(3)
        
        if choice == 1:
            pass