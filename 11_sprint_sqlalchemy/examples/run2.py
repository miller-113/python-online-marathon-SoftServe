from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, \
    text
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title


engine = create_engine('sqlite:///library1.db', echo=True)
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine) # bound session
session = Session()
author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')
book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)
# session.add(author_1)
# session.add(author_2)
# session.add(book_1)
# session.add(book_2)
# session.add(book_3)
# or simply session.add_all([author_1, author_2, book_1, book_2, book_3])
# session.commit()
book_3.description = u'Theory of evolution' # update the object
book_3 in session # check whether the object is in the session

session.commit()

session.query(Book).filter(Book.id == 1).all()

b = session.query(Book).filter(Book.id == 1)
b.one().description = 'Change text in item with id 1'
session.commit()    