from gestures import Gestures
from checkInputFunctions import (checkUserInputYesNo, checkUserInput)

class RockPaperScissors:
    def __init__(self) :
        self.gestures = Gestures()
        self.welcomeMessage()
    

    
    def thisRound():
        pass
    
    
    def checkRoundWinner(inputOne, inputTwo):
        if inputOne == inputTwo:
            print ("Tie! Play again!")
        else:
            pass
    
    def welcomeMessage(self):
        yesOrNo = input("Hello! Welcome to 'Rock Paper Scissors Lizard Spock'! Would you like to view the rules? ")
        yesOrNo = checkUserInputYesNo(yesOrNo)
        if yesOrNo == "yes":
            print ("""
                    Rock crushes Scissors
                    Scissors cuts Paper
                    Paper covers Rock
                    Rock crushes Lizard
                    Lizard poisons Spock
                    Spock smashes Scissors
                    Scissors decapitates Lizard
                    Lizard eats Paper
                    Paper disproves Spock
                    Spock vaporizes Rock
                    """)
        else:
            pass