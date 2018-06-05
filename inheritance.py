class Animal:
    def __init__(self, name='', health=0):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -=5
        return self
    def display_health(self):
        print('Animal\'s health:', self.health)

animal1 = Animal("yes", 50)
animal1.walk().walk().walk().run().run().display_health()





class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1=Dog()
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.health = 170
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        super().display_health()
        print('I am a Dragon')
        return self


dragon1 = Dragon()
dragon1.display_health()

animal2 = Animal("animal2", 40)
animal2.display_health()
