class Animal:
    def __init__(self, name, species, age):
        self.__name = name      
        self.__species = species 
        self.__age = age       

    def display_info(self):

        print(f'Имя: {self.__name}, Вид: {self.__species}, Возраст: {self.__age}')
        
    def get_name(self): 
        return self.__name
    
    def get_species(self):
        return self.__species
        
    def get_age(self):
        return self.__age

class Shelter:
    def __init__(self):
        self.animals = []

    def add_animals(self, animal):
        self.animals.append(animal)
        
    def show_animals(self):
        if not self.animals:
            print("Этот список пуст")
        else:
            for animal in self.animals:
                animal.display_info()
    
    def find_by_species(self, species_name):
        found = False
        for animal in self.animals:
            if animal.get_species() == species_name:
                animal.display_info()
                found = True
        
        if not found:
            print(f"Нет животных вида '{species_name}'")
        
            


shelter = Shelter()

cat = Animal("grisha", "Кот", 1)
cat2 = Animal("pasha", "Кот", 1)
dog = Animal("Yura", "Собака", 4)

print(cat.get_name())
print(cat.get_species())
print(cat.get_age())
cat.display_info()

shelter.add_animals(cat)
shelter.add_animals(cat2)
shelter.add_animals(dog)

shelter.show_animals()

print(shelter.animals)
print("Все кошки:")
shelter.find_by_species("Кот")

print("Все птицы:")
shelter.find_by_species("Птица")
