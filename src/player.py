# This is a player class to define the attributes of player and some helper methods to get the information about a player
import string

# Player Class 
class Player:

    # Constructor for player class that will intialize name, health, strength, attack of a player
    def __init__(self, name : string, health : int, strength : int, attack : int) -> None:
        self.Name = name
        self.Health = health
        self.Strength = strength
        self.Attack = attack
        pass

    # To get the Name of the player 
    def getName(self)-> string:
        return self.Name
    
    # To get the Health value of the player 
    def getHealth(self) -> string:
        return self.Health
    
    # To get the Strength value of the player
    def getStrength(self) -> string:
        return self.Strength
    
    # To get the Attack value of the player
    def getAttack(self) -> string:
        return self.Attack
    
    # To take the damage points from the Attacker which will reduce strength of the player
    def getDamage(self, damage : int) -> None:
        self.Health -= damage
        if self.Health <= 0:
            self.Health = 0


