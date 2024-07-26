# Magical Arena Game 

## Description 
This is a simple turn-based combat simulation game where two players take turns attacking each other until one of them dies. Each player has health, strength, and attack attributes. The outcome of each attack and defense is determined by rolling dice.

## Game Rules 
1. Each player has health, strength, and attack attributes.
2. Players attack in turns.
3. The attacking player rolls an attacking dice (1-6) and the defending player rolls a defending dice (1-6).
4. The attack value multiplied by the dice roll determines the attack damage.
5. The strength value multiplied by the dice roll determines the defense value.
6. The difference between the attack damage and defense value reduces the defender's health.
7. The game ends when a player's health reaches 0.

## How to Run the game
1. Check if you have Python Already installed in your machine or install it by 
    ```sh
        python --version
    ```

2. Open the Magical Arena folder into the terminal by going to the path

3. Run the game:
    a. In the terminal execute the following code  
    ```sh
        python main.py
    ```
    b. provide the required details for players


## Design Overview

- `Player` class represents a player with health, strength, and attack attributes 
- `Arena` class handles the game dynamics between two players declaring methods to play turn 
- `Dice` class implements the Dice Functionality into our Game
- `Input` class handles the input details taken from the user
- `Main` class handles the Functionality to initialize everything and calling Arena Class


