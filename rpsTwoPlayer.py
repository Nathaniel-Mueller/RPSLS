from rpsParent import *

class RockPaperScissorsTwoPlayer(RockPaperScissors):
    
    
    def __init__(self, nameOne, nameTwo):
        self.player_one_name = nameOne
        self.player_two_name = nameTwo
        super().__init__(nameOne, nameTwo)
        self.welcomeMessage()
        
    def welcomeMessage(self):
        print(f"Welcome {self.player_one_name} and {self.player_two_name}! You have chosen the 2 player game!")
        s(2)    # See rpsParent line 3: time.sleep() = s()
        
    def playerChoice(self):
        string = input(f"{self.player_one}, please choose a gesture by typing its name or number. ")
        string = checkUserInput(string)
        self.current_gesture_player_one = string
        string = self.gestures.chooseGesture(self.player_one, self.current_gesture_player_one)
        string = input(f"{self.player_two}, please choose a gesture by typing its name or number. ")
        string = checkUserInput(string)
        self.current_gesture_player_two = string
        string = self.gestures.chooseGesture(self.player_two, self.current_gesture_player_two)
        print (f"{self.player_one} has chosen {self.current_gesture_player_one} and {self.player_two} has chosen {self.current_gesture_player_two}.")