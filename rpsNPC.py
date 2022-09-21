from rpsParent import RockPaperScissors
import random as r

class RockPaperScissorsNPC(RockPaperScissors,):
    
    
    def __init__(self, name):
        super().__init__()
        self.npc = "NPC"
        self.name = name
        self.welcomeMessage()
        
    def welcomeMessage(self):
        print(f"Welcome {self.name}! You have chosen the 1 player game!")        
        
