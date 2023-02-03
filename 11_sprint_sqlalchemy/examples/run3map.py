from sqlalchemy.orm import mapper, relation, backref
from run import books_table, authors_table


class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title


b = mapper(Book, books_table)
a = mapper(Author, authors_table, properties={
    'books': relation(Book, backref='author')
})