#Created a class for dinosuar
class Dinosuar:    
    def __init__(self, name, health_points) -> None:
        self.name = name
        self.health_points = health_points
        self.attack_power = 10
        pass
#Defined an _init_ function with name and health points as parameters
    def attack(self, opponent):
        opponent.health_points -= self.attack_power
        pass
#Dinfined an attack function with opponent parameter