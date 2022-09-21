from rpsNPC import *
from rpsTwoPlayer import RockPaperScissorsTwoPlayer
from checkInputFunctions import *

class Game:
    
    def __init__(self):
        self.playercount = 0
        
    
        
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