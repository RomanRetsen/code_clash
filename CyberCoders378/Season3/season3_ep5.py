
import random
import time

from Archer import Archer
from Mage import Mage
from Paladin import Paladin
from Rogue import Rogue
from Warrior import Warrior
from GameCharacter import GameCharacter

CLASSES = [Warrior, Mage, Rogue, Paladin, Archer]


# Basic initialisation and create one instance of a characters. it randomly selects one class and instance the proper
# character class with the name of the character being "first_name" + __name__ field of the class. So it should be
# "Character18, Mage"
def create_random_character(name: str) -> GameCharacter:
    ...
    # TODO fill me


#Perform the combat arena simulation between those 2 characters
def simulate_battle(character1: GameCharacter, character2: GameCharacter):

    #Loop until either character are knocked down
    while character1.health > 0 and character2.health > 0:
        ...
        # TODO fill me

        # Manage Character 1 Actions
          # 5% chances of doing a special attack
          # 95% chance of doing a normal attack

          # have character 2 defending

          # Manage if character 2 is knocked out
            # character 1 experience is increase by the amount of character2 max HP

            # if expericence > 250
              # level up

        # Manage Character 2 Actions
          # 5% chances of doing a special attack
          # 95% chance of doing a normal attack

          # have characters 1 defending

          # Manage if character 1 is knocked out
            # character 2 experience is increase by the amount of character1 max HP

            # if expericence > 250
              # level up



    #Combat is done, reset the characters health and for the next match
    character1.reset_health()
    character2.reset_health()


# This is the main of the simulator. It initiates the array of characters and start the simulation of 1000 matches
# facing 2 opponents at a time.
def main():
    # Basic initialisation and create the arrays of all chatacters
    random.seed(0)
    characters = [create_random_character(f"Character_{i+1}") for i in range(25)]

    # Loop for 1000 rounds of the simulated battle
    for i in range(1000):
        char1, char2 = random.sample(characters, 2)

        # Print an introduction for the match displaying the first and last name for both contextant
        print(f"****** NEW Battle #{i}, {char1.name}: Lv{char1.level}  VS  {char2.name}: Lv{char2.level} -> ", end="")
        simulate_battle(char1, char2)
        print("Round is completed !")

    # Sort the array of characters by the numbers of wins, decreasing
    characters = sorted(characters, key=lambda char: char.wins, reverse=True)

    # Print the 'flag'
    print("flag{" + f"{characters[0].name}_{characters[0].wins}_{characters[0].level}" + "}")


if __name__ == "__main__":
    main()
