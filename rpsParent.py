from gestures import Gestures
from checkInputFunctions import *
from time import sleep as s     # time.sleep() = s()

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
        
    def gameRounds(self):
        while self.first_player_rounds_won < 2 and self.second_player_rounds_won <2:
            print(f"Round {self.current_round}")
            self.gestures.listGestures()
            self.playerChoice()
            self.checkRoundWinner(self.current_gesture_player_one, self.current_gesture_player_two)
        if self.first_player_rounds_won == 2:
            print(f"Game over! {self.player_one} wins!")
        elif self.second_player_rounds_won == 2:
            print (f"Game over! {self.player_two} wins!")

    def playerChoice(self):   # Needs to be defined in parent class to use in parent methods
        pass
        

    def checkRoundWinner(self, inputOne, inputTwo):     # Gets each input and compares them to declare a round winner
        if inputOne == inputTwo:
            print ("Tie! Play again!")
        elif inputOne == "rock":
            if inputTwo == "scissors" or inputTwo == "lizard":
                print (f"{inputOne} beats {inputTwo}!")
                print (f"{self.player_one} wins this round!")
                self.first_player_rounds_won += 1
            elif inputTwo == "spock" or inputTwo == "paper":
                print(f"{inputTwo} beats {inputOne}!")
                print (f"{self.player_two} wins this round!")
                self.second_player_rounds_won += 1
        elif inputOne == "paper":
            if inputTwo == "rock" or inputTwo == "spock":
                print(f"{inputOne} beats {inputTwo}!")
                print (f"{self.player_one} wins this round!")
                self.first_player_rounds_won += 1
            elif inputTwo == "scissors" or inputTwo == "lizard":
                print(f"{inputTwo} beats {inputOne}!")
                print (f"{self.player_two} wins this round!")
                self.second_player_rounds_won += 1
        elif inputOne == "scissors":
            if inputTwo == "lizard" or inputTwo == "paper":
                print(f"{inputOne} beats {inputTwo}!")
                print (f"{self.player_one} wins this round!")
                self.first_player_rounds_won += 1
            elif inputTwo == "rock" or inputTwo == "spock":
                print(f"{inputTwo} beats {inputOne}!")
                print (f"{self.player_two} wins this round!")
                self.second_player_rounds_won += 1
        elif inputOne == "lizard":
            if inputTwo == "spock" or inputTwo == "paper":
                print(f"{inputOne} beats {inputTwo}!")
                print (f"{self.player_one} wins this round!")
                self.first_player_rounds_won += 1
            elif inputTwo == "scissors" or inputTwo == "rock":
                print(f"{inputTwo} beats {inputOne}!")
                print (f"{self.player_two} wins this round!")
                self.second_player_rounds_won += 1
        elif inputOne == "spock":
            if inputTwo == "rock" or inputTwo == "scissors":
                print(f"{inputOne} beats {inputTwo}!")
                print (f"{self.player_one} wins this round!")
                self.first_player_rounds_won += 1
            elif inputTwo == "lizard" or inputTwo == "paper":
                print(f"{inputTwo} beats {inputOne}!")
                print (f"{self.player_two} wins this round!")
                self.second_player_rounds_won += 1
        self.current_round += 1