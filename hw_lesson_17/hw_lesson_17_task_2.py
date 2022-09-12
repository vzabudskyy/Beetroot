"""Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class
                                                   and adds the book to the books list
                                                   for the current library.

- group_by_author(author: Author) - returns a list of all books
                                    grouped by the specified author

- group_by_year(year: int) - returns a list of all the
                             books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books"""


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, book):
        if isinstance(book, Book):
            record = None
            for i in self.books:
                if str(book) == str(i["book"]):
                    record = i
                    break
            if record is None:
                self.books.append({"book": book, "copies": [book]})
                if book.author not in self.authors:
                    self.authors.append(book.author)
            else:
                record["copies"].append(book)

    def group_by_author(self, author):
        result = [i["book"] for i in self.books if i["book"].author.name == author]
        return result

    def group_by_year(self, year):
        result = [i["book"] for i in self.books if i["book"].year == year]
        return result

    def __str__(self):
        string_form = ""
        for i in library.books:
            string_form += f"\n{i['book']}\nCopies: {len(i['copies'])}"
        return string_form

    def __repr__(self):
        return f"<class 'Library'>"


class Book:
    all_books_amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.all_books_amount += 1

    def __str__(self):
        author = str(self.author)
        return f"\nBook: {self.name}\nYear: {self.year}\nAuthor:\n{author[:author.index('Book')-1]}"

    def __repr__(self):
        return f"<class 'Book'>"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self. birthday = birthday
        self.books = []

    def write_new_book(self, book):
        if type(book) is dict and ["name", "year"] == [i for i in book.keys()]:
            writed_book = Book(book["name"], book["year"], self)
            self.books.append(writed_book)
            return writed_book
        else:
            raise ValueError

    def __str__(self):
        return f"Name: {self.name}\nCountry: {self.country}\nBirthday: {self.birthday}\nBooks: {self.books}"

    def __repr__(self):
        return f"<class 'Author'> books {self.books}"


if __name__ == "__main__":
    library = Library("Vernadskoho")

    taras_shevchenko = Author("Taras Shevchenko", "Ukraine", "9 March 1814")
    ts_book1 = taras_shevchenko.write_new_book({"name": "Kobzar", "year": "1840"})
    ts_book2 = taras_shevchenko.write_new_book({"name": "Gaidamaky", "year": "1841"})
    ts_book1_copy = taras_shevchenko.write_new_book({"name": "Gaidamaky", "year": "1841"})

    john_tolkien = Author("John Ronald Reuel Tolkien", "England", "3 January 1892")
    jrrt_book1 = john_tolkien.write_new_book({"name": "Hobbit", "year": "1937"})
    jrrt_book2 = john_tolkien.write_new_book({"name": "Lord of the rings", "year": "1954"})
    jrrt_book2_copy_1 = john_tolkien.write_new_book({"name": "Lord of the rings", "year": "1954"})
    jrrt_book2_copy_2 = john_tolkien.write_new_book({"name": "Lord of the rings", "year": "1954"})

    joanne_rowling = Author("Joanne Rowling", "England", "31 July 1965")
    jr_book1 = joanne_rowling.write_new_book({"name": "Harry Potter and The Philosopher's Stone", "year": 1997})
    jr_book2 = joanne_rowling.write_new_book({"name": "Harry Potter and The Prisoner of Azkaban", "year": 1999})
    jr_book3 = joanne_rowling.write_new_book({"name": "Harry Potter and The Chamber of Secrets", "year": 1998})

    library.new_book(ts_book1)
    library.new_book(ts_book2)
    library.new_book(ts_book1_copy)

    library.new_book(jrrt_book1)
    library.new_book(jrrt_book2)
    library.new_book(jrrt_book2_copy_1)
    library.new_book(jrrt_book2_copy_2)

    library.new_book(jr_book1)
    library.new_book(jr_book2)
    library.new_book(jr_book3)
