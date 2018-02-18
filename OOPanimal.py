class Animal(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -=1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def displayInfo(self):
        print "ANIMAL STATUS", "\n\nName:", self.name, "\nHealth:", self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()   # use super to call the animal __init__ method
        self.name = name
        self.health = 150           # every dog starts off with 150 health

    def pet(self):
        self.health += 5
        return self

# class dragon(animal):
#     def __init__(self):
#         super(animal, self).__init__()    # use super to call the Human __init__ method
#         self.stealth = 10                # every Ninja starts off with 10 stealth
#     def steal(self):
#         self.stealth += 5

animal1 = Animal("Liger")
dog1 = Dog("Spot")

#animal1.walk().run().displayInfo()
dog1.walk().walk().walk().run().run().pet().displayInfo()
