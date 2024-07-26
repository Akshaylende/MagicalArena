# This is Arena class where our Game mechanics and logic is imprinted 
 
from src.player import Player
from src.dice import Dice

# Implementing Arena Class 
class Arena:
    # Initializing the players and Dice and calling startMatch to start the game
    def __init__(self, player1 : Player, player2 : Player, dice : Dice) -> None:
        self.playerA = player1
        self.playerB = player2
        self.dice = dice
        self.startMatch()


    # This method will start the match 
    def startMatch(self) -> None:
        start = True

        # starting the match till any player's health reaches zero
        while(self.playerA.getHealth() > 0  and self.playerB.getHealth() > 0):
            # To check for the first time 
            if (start == False or self.playerA.getHealth() <= self.playerB.getHealth()):
                self.playTurn(self.playerA, self.playerB)
                if self.checkAlive(self.playerB) == False:
                    self.winner(self.playerA)
                    break

            start = False
            
            # Altering the player's Turn 
            self.playTurn(self.playerB, self.playerA)
            if self.checkAlive(self.playerA) == False:
                self.winner(self.playerB)
                break


    # This method is used to play turn by players 
    def playTurn(self, attacker : Player, defender : Player) -> None:
        pass 


    # This method is used to check if the player is Alive 
    def checkAlive(self, player : Player) -> bool:
        if player.getHealth() == 0:
            return False
        return True


    
