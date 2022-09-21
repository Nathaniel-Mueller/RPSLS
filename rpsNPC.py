from rpsParent import RockPaperScissors
import random as r

class RockPaperScissorsNPC(RockPaperScissors):
    def __init__(self):
        super().__init__()
        self.welcomeMessage()
        
    def welcomeMessage(self):
        print("You have chosen the 1 player game!")
        
