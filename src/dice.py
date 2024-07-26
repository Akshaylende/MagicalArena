# This is a Dice class to Initialize and Implement Dice Functionality into our Game
import random

# Dice Class
class Dice:
    def __init__(self) -> None:
        pass
    
    # Implementing the Dice Functionality using random number generator 
    def roll(self) -> int:
        return random.randint(1,6)