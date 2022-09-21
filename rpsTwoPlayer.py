from rpsParent import RockPaperScissors

class RockPaperScissorsTwoPlayer(RockPaperScissors):
    def __init__(self) -> None:
        super().__init__()
        self.welcomeMessage()
        
    def welcomeMessage(self):
        print("You have chosen the 2 player game!")
        
