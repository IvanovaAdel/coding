class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f'Имя: {self.name}, Вид: {self.species}, Возраст: {self.age}')

class Shelter:
    def __init__(self):
        self.animals = []

    def add_animals(self, animal):
        self.animals.append(animal)

shelter = Shelter()

cat = Animal("grisha", "fsde", 1)

print(cat.name)
print(cat.species)
print(cat.age)
cat.display_info()

shelter.add_animals(cat)
print(shelter.animals)
