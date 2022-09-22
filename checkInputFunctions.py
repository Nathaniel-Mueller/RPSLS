from tkinter import W


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
    numberedInputs = ["1", "2", "3", "4", "5"]
    userInput = userInput.casefold()
    if userInput in numberedInputs:
        if userInput == "1":
            userInput = "rock"
        elif userInput == "2":
            userInput = "paper"
        elif userInput == "3":
            userInput = "scissors"
        elif userInput == "4":
            userInput = "lizard"
        elif userInput == "5":
            userInput = "spock"
    if userInput in correctInputs:
        pass
    else:
        while userInput not in correctInputs:
            userInput = input("I'm sorry, that was an incorrect input, please try again! ")
            userInput = userInput.casefold()
    return userInput

def checkIfNumber(userInput):
    while isinstance(userInput, str): 
        if userInput.isdigit() == True:
            userInput = int(userInput)
        else:
            while userInput.isdigit() == False:
                userInput = input("I'm sorry, that wasn't a number, please try again. ")
                if userInput.isdigit() == True:
                    userInput = int(userInput)
                    return userInput
    else:
        pass
    return userInput

def checkNumberRange(userInput):
        userInput = checkIfNumber(userInput)
        while userInput > 2 or userInput < 1:
            if userInput > 2:
                userInput = input("That's too many players! Please try again. ")
                userInput = checkIfNumber(userInput)  
            elif userInput < 1:
                userInput = input("You have to select at least one player! Please try again. ")
                userInput = checkIfNumber(userInput)
        return userInput

