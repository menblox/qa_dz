class Cat():

    species = "кот"

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50

    def meow(self):
        return "Мяу!"

    def feed(self, amount):
        if self.hunger - amount > 0:
            self.hunger = self.hunger - amount
            return self.hunger
        else:
            self.hunger = 0
            return self.hunger

    def is_hungry(self):
        if self.hunger > 20: return True
        else: return False

    @classmethod
    def get_species(cls):
        return cls.species


a = Cat("Барс", "Red")

print(a.meow())
print(a.feed(1))
print(a.is_hungry())
print(a.get_species())