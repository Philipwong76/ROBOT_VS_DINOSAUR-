class Dinosuar:
    def __init__(self, name, health_points) -> None:
        self.name = name
        self.health_points = health_points
        self.attack_power = 10
        pass

    def attack(self, opponent):
        opponent.health_points -= self.attack_power
        pass