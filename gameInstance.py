from rpsNPC import *
from rpsTwoPlayer import RockPaperScissorsTwoPlayer
from checkInputFunctions import *

class Game:
    
    def __init__(self):
        self.player_count = 0
        self.player_names = []
        self.chosenMode = __class__
        
    
        
    def welcomeMessage(self):
        yesOrNo = input("Hello! Welcome to 'Rock Paper Scissors Lizard Spock'! Each game will be played best 2 out of 3. Would you like to view the rules? ")
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
        self.getPlayerNames(self.player_count)
        self.chooseMode(self.player_count)
        self.chosenMode.gameRounds()
        
    
    def chooseMode(self, input):
        if input == 1:
            self.chosenMode = RockPaperScissorsNPC(self.player_names[0])
        elif input == 2:
            self.chosenMode = RockPaperScissorsTwoPlayer(self.player_names[0], self.player_names[1])
        
    def getPlayerNames(self, userInput):
        if userInput == 1:
            playerOne = input ("Please enter your name. ")
            playerOne = checkEmptyString(playerOne)
            self.player_names.append(playerOne)
        elif userInput == 2:
            playerOne = input("Player one, please enter your name. ")
            playerOne = checkEmptyString(playerOne)
            self.player_names.append(playerOne)
            playerTwo = input("Player two, please enter your name. ")
            playerTwo = checkEmptyString(playerTwo)
            self.player_names.append(playerTwo)