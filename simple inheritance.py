# App demonstrating object oriented single inheritance 
# The parent class "Batallion" creates new child class "Soldier" instances using the "recruit()" method

global soldier_arr
soldier_arr = []

class Batallion:
    def __init__(self, batallion_name):
        self.batallion_name = batallion_name
        
    def recruit(self, soldier_name):
        for i in soldier_name:
            soldier_arr.append(Soldier(i))

class Soldier(Batallion):
    def __init__(self, soldier_name):
        self.soldier_name = soldier_name

a_team = Batallion("A Team")
a_team.recruit(["Mr. T", "Steve McQueen", "Danny Devito", "Ryan Aerhart", "Kerry Fischer"])

print(soldier_arr[0].soldier_name)