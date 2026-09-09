class Book:
    page_material = "бумага"
    has_text = True

    def __init__(self, title, author, page_count, isbn, is_reserved):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def get_status(self):
        return ", зарезервирована" if self.is_reserved else ""

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}"

    def book_info(self):
        return self.get_info() + ", материал: " + self.page_material + self.get_status()


class SchoolBook(Book):
    def __init__(
        self, title, author, page_count, isbn,
        is_reserved, subject, school_class, has_exercises
    ):
        super().__init__(title, author, page_count, isbn, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

    def get_school_info(self):
        return f"предмет: {self.subject}, класс: {self.school_class}"

    def school_info(self):
        return super().get_info() + ", " + self.get_school_info() + super().get_status()


book_1 = Book(
    "Идиот", "Достоевский", 500,
    "3425-17-090455-3", False
)
book_2 = Book(
    "Мастер и Маргарита", "Булгаков", 480,
    "97225-17-091978-6", False
)
book_3 = Book(
    "1984", "Оруэлл", 328,
    "5420-452-28423-4", False
)
book_4 = Book(
    "Преступление и наказание", "Достоевский", 672,
    "9725-17-089996-5", False
)
book_5 = Book(
    "Три товарища", "Ремарк", 480,
    "978-5-17-090164-3", False
)

school_book_1 = SchoolBook(
    "Алгебра", "Иванов", 200, "978-5-17-000000-1",
    False, "Математика", 9, True
)
school_book_2 = SchoolBook(
    "География", "Сидоров", 180, "978-5-17-000000-3",
    False, "География", 7, False
)

book_1.is_reserved = True
school_book_1.is_reserved = True

print(
    book_1.book_info(),
    book_2.book_info(),
    book_3.book_info(),
    book_4.book_info(),
    book_5.book_info(),
    school_book_1.school_info(),
    school_book_2.school_info(),
    sep="\n"
)
