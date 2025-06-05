class Student:
    def __init__(self,  name, student_id):
        self.name = name
        self.student_id = student_id
    
    def display_info(self):
        print(f"Имя: {self.name}, ID: {self.student_id}")
        
class Group:
    def  __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(self.students)
        
    def show_students(self):
        if not self.students:
            print("Группа пуста.")
        else:
            for student in self.students:
                student.display_info()
group = Group()
stud1 = Student("Grisha", 1)
stud2 = Student("Masha" , 2)
stud1.display_info()
group.add_student(stud1)
group.add_student(stud2)
group.show_students()
