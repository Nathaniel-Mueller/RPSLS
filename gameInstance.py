from rpsNPC import *
from rpsTwoPlayer import RockPaperScissorsTwoPlayer
from checkInputFunctions import *

class Game:
    
    def __init__(self):
        self.player_count = 0
        self.player_names = []
        
    
        
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
        
    def runGame(self):
        self.welcomeMessage()
        self.player_count = input("Please enter the number of players, 1 or 2: ")
        self.player_count = checkNumberRange(self.player_count)
        self.chooseMode(self.player_count)
        
    
    def chooseMode(self, input):
        if input == 1:
            select = RockPaperScissorsNPC()
            return select
        elif input == 2:
            select = RockPaperScissorsTwoPlayer()
            return select
        
    def playerNames(self, userInput):
        if userInput == 1:
            self.player_names.append(input("Please enter your name. "))
        elif userInput == 2:
            playerOne = input("Player one, please enter your name. ")
            playerTwo = input("Player two, please enter your name. ")
            self.player_names.append(playerOne)
            self.player_names.append(playerTwo)