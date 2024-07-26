# This will the entry point to run the Game 

# Importing Dependency classes 
from src.input import Input
from src.dice import Dice
from src.arena import Arena 


# Here we will Initialize our Game and setup
def main() -> None:
    print("Welcome to the Magical Arena!")

    print("Are you ready to take a deep dive into this magical world ?")
    play = input("press Y for Yes or N for No : ")

    if play == "Y":
        # Initializing Input class instance to take inputs
        inputs = Input()
        
        # Taking player details from the input 
        print("Player 1")
        player1 = inputs.playerDetails()
        print("Player 2")
        player2 = inputs.playerDetails()
        
        # Initializing Dice class instance to roll 
        dice = Dice()

        # Initializing Arena class instance to run our game mechanics
        Arena(player1, player2, dice)
    

    
# calling the main Function
if __name__ == "__main__" :
    main()