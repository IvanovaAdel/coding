import json
import os

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        return f'"{self.name}", {self.author}, {self.year}'

    def to_dict(self):
        return {
            'name': self.name,
            'author': self.author,
            'year': self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['author'], data['year'])


class Library:
    def __init__(self, filename="library.json"):
        self.books = []
        self.filename = filename
        self.load()

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга {book.get_info()} добавлена в список')
        self.save()

    def remove_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                print(f'Книга "{book_name}" удалена из библиотеки.')
                self.save()
                return
        print(f'Книга "{book_name}" не найдена.')

    def show_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
            return
        print("Список книг в библиотеке:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.get_info()}")

    def save(self):
        data = [book.to_dict() for book in self.books]
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Данные успешно сохранены в файл.")
        except IOError as e:
            print(f"Ошибка при сохранении файла: {e}")

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]
            print("Данные библиотеки успешно загружены.")
        except FileNotFoundError:
            print("Файл с данными не найден. Будет создан новый при сохранении.")
        except json.JSONDecodeError:
            print("Ошибка чтения файла: неверный формат данных.")
        except Exception as e:
            print(f"Неизвестная ошибка при загрузке: {e}")


def main():
    menu = """
Введите:
1 - добавить книгу
2 - удалить выбранную книгу
3 - показать список книг
4 - выйти
"""

    lib = Library()

    while True:
        choice = input(menu)
        
        if choice == "1":
            name = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            try:
                year = int(year)
                lib.add_book(Book(name, author, year))
            except ValueError:
                print("Год должен быть числом!")
        
        elif choice == '2':
            name = input("Введите название книги для удаления: ")
            lib.remove_book(name)
        
        elif choice == '3':
            lib.show_books()
        
        elif choice == '4':
            print("Сохранение данных и выход из программы.")
            lib.save()
            break
        
        else:
            print("Неверный ввод. Пожалуйста, выберите 1-4.")


if __name__ == "__main__":
    main()
