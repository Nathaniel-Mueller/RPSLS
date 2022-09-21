from gestures import Gestures
from checkInputFunctions import *

class RockPaperScissors:
    def __init__(self) :
        self.gestures = Gestures()
        
    

        

    def checkRoundWinner(inputOne, inputTwo):
        if inputOne == inputTwo:
            print ("Tie! Play again!")
        elif inputOne == "rock" and inputTwo == "scissors":
            pass
