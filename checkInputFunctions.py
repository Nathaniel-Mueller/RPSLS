def checkUserInputYesNo(userInput):
        userInput = userInput.casefold()
        if userInput == "yes" or userInput == "no":
            pass
        else:
            while userInput != "yes" and userInput != "no":
                userInput = input("I'm sorry that's an incorrect input, please try again! ")
                userInput = userInput.casefold()
        return userInput
    
def checkUserInput(userInput):
    correctInputs = ["rock", "paper", "scissors", "lizard", "spock"]
    userInput = userInput.casefold()
    if userInput in correctInputs:
        pass
    else:
        while userInput not in correctInputs:
            userInput = input("I'm sorry, that was an incorrect input, please try again! ")
            userInput = userInput.casefold()
    return userInput