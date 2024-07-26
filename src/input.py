# This is a Input class to get the information about a player attributes from user for the game

from src.player import Player

# Input class
class Input:
    # constructor to Initialize Input class
    def __init__(self) -> None:
        print("Enter the Player Details for")
        pass

    # Method to take the input about player attributes from user
    def playerDetails(self) -> Player:
        name = input("Name : ")
        health = int(input("Health : "))
        strength = int(input("Strength : "))
        attack = int(input("Attack : "))
        print(" ")
        
        # Returning player Instance to the calling place  
        return Player(name, health, strength, attack)
