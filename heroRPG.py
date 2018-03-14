class Hero:
    def __init__ (self,name):
        self.name = name
        self.health = 10
        self.power = 5
    
    def attack(self, goblin):
        goblin.health -= self.power
        print("{} does {} damage to {}.".format(self.name,self.power,goblin.name))
        if goblin.health <= 0:
                print("{} is dead.".format(goblin.name))
        
        
        
class Goblin:
    def __init__ (self, name):
        self.name = name
        self.health = 6
        self.power = 2