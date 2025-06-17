class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')


class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):  
        self.books.append(book)
        print(f'Книга "{book.name}" добавлена в список')

    def remove_book(self, book_name):
        for book in self.books:  
            if book.name == book_name:
                self.books.remove(book)
                print(f'Книга "{book_name}" удалена из библиотеки.')
                return
        print(f'Книга "{book_name}" не найдена.')

    def show_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
            return
        print("Список книг в библиотеке:")
        for book in self.books:
            book.get_info()

        
lib = Library()
b1 = Book("fed","re",1999)
b2 = Book("saz","re",1999)
b3 = Book("fdrg","re",1999)
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.remove_book("fed")
lib.show_books()
