def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__grades = []
        
    def get_name(self):
        return self.__name
        
    def get_student_id(self):
        return self.__student_id
        
    def get_grades(self):
        return self.__grades
        
    def display_info(self):
        print(f"Имя: {self.__name}, ID: {self.__student_id}")
        
    def add_grade(self, grade):
        self.__grades.append(grade)
        
    def get_average(self):
        return sum(self.__grades) / len(self.__grades)
        
class Group:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Добавлен студент: {student.get_name()}") 
        
    def show_students(self):
        if not self.students:
            print("Группа пуста.")
        else:
            for student in self.students:
                student.display_info()
                
    def find_by_name(self, name):
        found = False
        for student in self.students:
            if name == student.get_name():
                student.display_info()
                found = True
            if not found:
                print("Студент не найден")
            


# Использование
group = Group()
stud1 = Student("Grisha", 1)
stud2 = Student("Masha", 2)

stud1.add_grade(5)
stud1.add_grade(4)
stud1.add_grade(3)
stud2.add_grade(4)
stud2.add_grade(5)

stud1.display_info()
group.add_student(stud1)
group.add_student(stud2)

group.show_students()

print(f"Средний балл Grisha: {stud1.get_average()}")
print(f"Средний балл Masha: {stud2.get_average()}")
group.find_by_name("Grisha")
