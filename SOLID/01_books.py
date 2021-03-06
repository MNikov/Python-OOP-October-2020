class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        searched = [b for b in self.books if b.title == title]
        if searched:
            book = searched[0]
            return f'We have the book {title}'

