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
group = Group()
stud1 = Student("Grisha", 1)
stud1.display_info()
group.add_student(stud1)
