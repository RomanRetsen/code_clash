from abc import ABC, abstractmethod


# Base class
class GameCharacter(ABC):
    # Constructor method for Generic class for a game character. It initiated the basic attributes of all classes:
    # name from the argument 1; health and max_health from argument 2; level to 1; experience to 0; wins to 0
    def __init__(self, name: str, max_health: int):
        self.name = name
        self.max_health = max_health

    # Abstract method for the attack. It is empty here but are overloaded in sub-classes for each character classes
    # specific attacks
    @abstractmethod
    def attack(self) -> int:
        pass

    # Abstract method for defend. It is empty here but are overloaded in sub-classes for each character classes
    # specific defend.
    @abstractmethod
    def defend(self, damage: int) -> int:
        pass

    # Abstract method for the special ability. It is empty here but are overloaded in sub-classes for each character
    # classes specific special ability
    @abstractmethod
    def special_ability(self) -> (str, int):
        pass

    # Generic method for the leveling up. It is the same for each character classes, so it doesn't need to be
    # overloaded.
    def level_up(self):
        ...
        # TODO: fill me

    # Abstract method for the improved_stats. Called whenever a character change level to adjust its characteristic.
    # Since it will be different character classes, it is empty here but are overloaded in sub-classes for each
    # character classes specific stats adjustments.
    @abstractmethod
    def improve_stats(self):
        pass

    # Generic method for the reset health from the max_health attribute. It is the same for each character classes, so
    # it doesn't need to be overloaded.
    def reset_health(self):
        ...
        # TODO: fill me
