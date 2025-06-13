from book import Book


library = [
    Book('Маленький принц', 'Экзюпери'),
    Book('Гарри Поттер', 'Роулинг'),
    Book('Три мушкетера', 'Дюма')
]

for book in library:
    print(f'{book.tit} - {book.aut}')
