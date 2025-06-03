class Animal:
    def __init__(self, name, species, age):
       self.name = name
       self.species = species
       self.age = age

    def display_info(self):
        print(f'Имя: {self.name}, Вид:{self.species} , Возраст:{self.age} ')
        
    
cat = Animal("grisha", "fsde", 1)
print(cat.name)
print(cat.species)
print(cat.age)
print(cat.display_info())
