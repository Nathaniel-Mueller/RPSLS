from rpsParent import RockPaperScissors
import random as r

class RockPaperScissorsNPC(RockPaperScissors):
    
    
    def __init__(self, name):
        self.npc = "NPC"
        self.name = name
        super().__init__(name, self.npc)
        self.welcomeMessage()
        
        
    def welcomeMessage(self):
        print(f"Welcome {self.name}! You have chosen the 1 player game!")        
        
