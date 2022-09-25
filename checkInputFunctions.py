# List of input check functions to import to other classes

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
    userInput = numberToGesture(userInput)
    if userInput in correctInputs:
        pass
    else:
        while userInput not in correctInputs and userInput not in numberedInputs:
            userInput = input("I'm sorry, that was an incorrect input, please try again! ")
            userInput = userInput.casefold()
            userInput = numberToGesture(userInput)
    return userInput

def checkIfNumber(userInput):       # Determine if userInput is a number, even if it's a string
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

def checkNumberRange(userInput):        # Checks to make sure amount of players selected is within range
        userInput = checkIfNumber(userInput)
        while userInput > 2 or userInput < 1:
            if userInput > 2:
                userInput = input("That's too many players! Please try again. ")
                userInput = checkIfNumber(userInput)  
            elif userInput < 1:
                userInput = input("You have to select at least one player! Please try again. ")
                userInput = checkIfNumber(userInput)
        return userInput

def numberToGesture(userInput):     # Allows user to input numbers instead of whole words for chooseGesture
    numberedInputs = ["1","2","3","4","5"]
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
    return userInput

def checkEmptyString (userInput):       # Check if name input is empty or only spaces
    while userInput == "" or userInput.isspace() == True:
        userInput = ("You have to enter something! Please try again. ")
    return userInput
