from rpsParent import *
from random import choice as rc

class RockPaperScissorsNPC(RockPaperScissors):
    
    
    def __init__(self, name):
        self.npc = "NPC"
        self.name = name
        super().__init__(name, self.npc)
        self.welcomeMessage()
        
        
    def welcomeMessage(self):
        print(f"Welcome {self.name}! You have chosen the 1 player game!")
        s(2)    # See rpsParent line 3: time.sleep() = s()
        
    def getNPCGesture(self):        # Selects a random gesture for the NPC
        choice = rc(self.gestures.available_gestures)
        return choice
    
    def playerChoice(self):     # Get gesture input from player and assign random to NPC
        string = input(f"{self.player_one}, please choose a gesture by typing its name or number. ")
        string = checkUserInput(string)
        self.current_gesture_player_one = string
        self.gestures.chooseGesture(self.player_one, self.current_gesture_player_one)
        self.current_gesture_player_two = self.getNPCGesture()
        self.gestures.chooseGesture(self.player_two, self.current_gesture_player_two)
        print (f"{self.player_one} has chosen {self.current_gesture_player_one} and {self.player_two} has chosen {self.current_gesture_player_two}.")