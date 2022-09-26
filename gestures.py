from checkInputFunctions import *
from time import sleep as s

class Gestures:
    
    def __init__(self):
        self.available_gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.current_gesture = ""
        
            
    def chooseGesture(self, selectedPlayer, gestureChoice):
        self.current_gesture = checkUserInput(gestureChoice)
        print (f"{selectedPlayer} has chosen a gesture.")
        s(1)
        return self.current_gesture
    
    def listGestures(self):
        number = 1
        print ("Your available gestures are:")
        for gestures in self.available_gestures:
            print(f"{number}: {gestures}")
            s(.5)
            number += 1