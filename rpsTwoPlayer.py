from rpsParent import RockPaperScissors

class RockPaperScissorsTwoPlayer(RockPaperScissors):
    
    
    def __init__(self, nameOne, nameTwo):
        self.player_one_name = nameOne
        self.player_two_name = nameTwo
        super().__init__(nameOne, nameTwo)
        self.welcomeMessage()
        
    def welcomeMessage(self):
        print(f"Welcome {self.player_one_name} and {self.player_two_name}! You have chosen the 2 player game!")
        
