# from gestures import Gestures

class RockPaperScissors:
    def __init__(self) :
        self.correct_inputs = ["rock", "paper", "scissors", "lizard", "spock"]
       # self.gestures = Gestures()
        self.welcomeMessage()
    
    def checkUserInputYesNo(self, userInput):
            userInput = userInput.casefold()
            if userInput == "yes" or userInput == "no":
                pass
            else:
                while userInput != "yes" and userInput != "no":
                    userInput = input("I'm sorry that's an incorrect input, please try again! ")
                    userInput = userInput.casefold()
            return userInput
    def checkUserInput(self, userInput):
        userInput = userInput.casefold()
        if userInput in self.correct_inputs:
            pass
        else:
            while userInput not in self.correct_inputs:
                userInput = input("I'm sorry, that was an incorrect input, please try again! ")
                userInput = userInput.casefold()
        return userInput
    
    
    def welcomeMessage(self):
        yesOrNo = input("Hello! Welcome to 'Rock Paper Scissors Lizard Spock'! Would you like to view the rules? ")
        yesOrNo = self.checkUserInputYesNo(yesOrNo)
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