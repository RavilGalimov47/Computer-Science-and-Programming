class book:
    def __init__(self, title, author, year, page_count):
        self.title = title
        self.author = author
        self.year = year
        self.page_count = page_count

    def __str__(self):
        print(f"Название книги: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Кол-во страниц: {self.page_count}")


book1 = book("Кладбище домашних животных", "Стивен Кинг", 1983, 426)
book2 = book("1984", "Джордж Оруэлл", 1949, 328)
book3 = book("Вокруг света за 80 дней", "Жюль Верн", 1872 , 240)

print("\nПервая книга:")
book1.__str__()
print("\nВторая книга:")
book2.__str__()
print("\nТретья книга:")
book3.__str__()