from rpsNPC import *
from rpsTwoPlayer import RockPaperScissorsTwoPlayer
from checkInputFunctions import *

class Game:
    
    def __init__(self):
        self.player_count = 0
        self.player_names = []
        self.chosenMode = __class__
        
    
        
    def welcomeMessage(self):
        yesOrNo = input("Hello! Welcome to \"Rock Paper Scissors Lizard Spock\"!\nEach game will be played best 2 out of 3. Would you like to view the rules? ")
        yesOrNo = checkUserInputYesNo(yesOrNo)
        s(1)
        if yesOrNo == "yes":
            print ("Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")
        else:
            pass
    def runGame(self):
        self.welcomeMessage()
        while True:
            self.player_count = input("Please enter the number of players, 1 or 2: ")
            self.player_count = checkNumberRange(self.player_count)
            self.getPlayerNames(self.player_count)
            self.chooseMode(self.player_count)
            self.chosenMode.gameRounds()
            string = input("Would you like to play another game? ")
            string = checkUserInputYesNo(string)
            if string == "yes":
                pass
            elif string == "no":
                print ("Thanks for playing!")
                break           
            
    
    def chooseMode(self, input):        # Select a class based on amount of players entered
        if input == 1:
            self.chosenMode = RockPaperScissorsNPC(self.player_names[0])
        elif input == 2:
            self.chosenMode = RockPaperScissorsTwoPlayer(self.player_names[0], self.player_names[1])
        
    def getPlayerNames(self, userInput):        # Grab names from input and assign to player(s)
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