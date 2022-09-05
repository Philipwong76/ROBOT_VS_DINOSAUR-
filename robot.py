#Created a robot class
class Robot:
    def __init__(self, name, health_points ) -> None:
        self.name = name
        self.health_points = health_points
        self.weapon = 
        pass
#Defined a _init_ function with name and health points as parameters, yet to introduce weapon class at the moment
    def attack(self, opponent):
        opponent.health_points -= self.weapon.attack
        pass
#Defined an attack function with opponent as parameter