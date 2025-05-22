from abc import ABC, abstractmethod

class LibraryUser(ABC):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    @abstractmethod
    def borrow_book(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass


class Student(LibraryUser):
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f"Студент {self.name} не может взять больше 3 книг")
            return False
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"Студент {self.name} взял книгу '{book.title}'")
        else:
            print(f"Книга '{book.title}' недоступна")
            

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"Студент {self.name} вернул книгу '{book.title}'")
         
         
        else:
            print(f"У студента {self.name} нет книги '{book.title}'")
            
