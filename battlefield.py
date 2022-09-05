#Import robot class from robot module
#Import dinosuar Class from robot module
from robot import Robot
from dinosuar import Dinosuar

#Created a battlefield class 
class Battlefield:
#Defined functions specifically setting a parameter for 2 variables
    def __init__(self) -> None:
        self.robot = Robot('robot', 100)
        self.dinosuar = Dinosuar('dinosuar', 100)
        pass
#Imported each class in its respective variable and identify it's string name with 100 health points each
    def battle(self):
        while (self.robot.health_points > 0 or self.dinosuar.health_points > 0):
            self.robot.attack(self.dinosuar)
            self.dinosuar.attack(self.robot)
            print('Robot attacks dinosuar')
            print(f'Dinosuar health:' , self.dinosuar.health_points)
            print('Dinosuar attacks robot')
            print(f'Robot health:' , self.robot.health_points)
        if self.robot.health_points < self.dinosuar.health_points:
            self.winner(self.dinosuar)
        elif self.dinosuar.health_points < self.robot.health_points:
            self.winner(self.robot)    
#Created a while loop to ensure that robot will win in this defined function called 'battle'
#Within the while loop, created a print function indivdual to show both the dinosuar and robots health after each attack.
    def run(self):
        self.greeting()
        self.battlephrase()
        self.battle()
        print(f'Congrulations the winner is ' + self.winner.name)
        pass
#Defined a run function to allow each defined functions below to be called in it's respective order.
#Defined a winner function that has a self parameter with a pulled function of winner equals to that of the variable TheWinner.(the parameters are used for the if and elif statements within the while loop)

    def winner(self, TheWinner):
        self.winner = TheWinner
        pass
    

    def greeting(self):
        print("Welcome to the battlefield between a mechanical machine against a prehistoric lizard!!!")

    def battlephrase(self):
        print('Get Ready to Rumble!')

    