from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref, registry
import logging

logging.disable(logging.WARNING)

mapper_registry = registry()

Base = mapper_registry.generate_base()


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
        return f'Id:  {self.id}\n' \
               f'title:  {self.title}\n' \
               f'description:  {self.description}\n' \
               f'author_id:  {self.author_id}\n'


engine = create_engine('sqlite:///library4.db')
Base.metadata.create_all(engine)
print('Connected to SQLite')
Session = sessionmaker(bind=engine)
session = Session()
author1 = Author('Gina')
author2 = Author('Faren')
book1 = Book('Title1', 'description1', author1)
book2 = Book('Title2', 'description2', author1)
book3 = Book('Title3', 'description3', author1)
# [session.add(i) for i in [author1, author2, book1, book2, book3]]
session.add(author1)
session.add(book1)
session.commit()

query = session.query(Book).all()
# print(f'Total rows are:   {len(query)}')
# print('Printing each row')
# for item in query:
#     print(f'{item}\n')




