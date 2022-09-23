from gestures import Gestures
from checkInputFunctions import *

class RockPaperScissors:
    
    
    def __init__(self,name,name2) :
        self.gestures = Gestures()
        self.current_round = 1
        self.player_one = name
        self.player_two = name2
        self.first_player_rounds_won = 0
        self.second_player_rounds_won = 0
        self.current_gesture_player_one = ""
        self.current_gesture_player_two = ""
        
    def gameRound(self):
        while self.first_player_rounds_won < 2 and self.second_player_rounds_won <2:
            print(f"Round {self.current_round}")
            self.gestures.listGestures()
            self.playerChoice()

    def playerChoice(self):
        string = input(f"{self.player_one}, please choose a gesture by typing its name or number. ")
        string = checkUserInput(string)
        self.current_gesture_player_one = string
        string = self.gestures.chooseGesture(self.player_one, self.current_gesture_player_one)
        string = input(f"{self.player_two}, please choose a gesture by typing its name or number. ")
        string = checkUserInput(string)
        self.current_gesture_player_two = string
        string = self.gestures.chooseGesture(self.player_two, self.current_gesture_player_two)
        

    def checkRoundWinner(self, inputOne, inputTwo):
        if inputOne == inputTwo:
            print ("Tie! Play again!")
        elif inputOne == "rock":
            if inputTwo == "scissors" or inputTwo == "lizard":
                print (f"{inputOne} beats {inputTwo}!")
            elif inputTwo == "spock" or inputTwo == "paper":
                print(f"{inputTwo} beats {inputOne}!")
        elif inputOne == "paper":
            if inputTwo == "rock" or inputTwo == "spock":
                print(f"{inputOne} beats {inputTwo}!")
            elif inputTwo == "scissors" or inputTwo == "lizard":
                print(f"{inputTwo} beats {inputOne}!")
        elif inputOne == "scissors":
            if inputTwo == "lizard" or inputTwo == "paper":
                print(f"{inputOne} beats {inputTwo}!")
            elif inputTwo == "rock" or inputTwo == "spock":
                print(f"{inputTwo} beats {inputOne}!")
        elif inputOne == "lizard":
            if inputTwo == "spock" or inputTwo == "paper":
                print(f"{inputOne} beats {inputTwo}!")
            elif inputTwo == "scissors" or inputTwo == "rock":
                print(f"{inputTwo} beats {inputOne}!")
        elif inputOne == "spock":
            if inputTwo == "rock" or inputTwo == "scissors":
                print(f"{inputOne} beats {inputTwo}!")
            elif inputTwo == "lizard" or inputTwo == "paper":
                print(f"{inputTwo} beats {inputOne}!")
        self.current_round += 1