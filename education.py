class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        
    def display_info(self):
        print(f"Имя: {self.name}, ID: {self.student_id}")
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def get_average(self):
        return sum(self.grades) / len(self.grades)
        
class Group:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Добавлен студент: {student.name}")
        
    def show_students(self):
        if not self.students:
            print("Группа пуста.")
        else:
            for student in self.students:
                student.display_info()

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
