#Created a robot class
from weapon import Weapon
#import weapon class from weapon module
class Robot:
    def __init__(self, name, health_points ) -> None:
        self.name = name
        self.health_points = health_points
        self.weapon = Weapon('laser', 11)
        pass
#Defined a _init_ function with name and health points as parameters, yet to introduce weapon class at the moment
#Added weapon class with spring parameter name and created 11 attack points for weapon class.
    def attack(self, opponent):
        opponent.health_points -= self.weapon.attack
        pass
#Defined an attack function with opponent as parameter