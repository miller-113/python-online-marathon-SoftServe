from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref, registry
import logging

logging.disable(logging.WARNING)

mapper_registry = registry()

Base = mapper_registry.generate_base()



class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    City = Column(String)
    Grade = Column(Integer)
    Salesperson_id = Column(Integer)

    def __init__(self, name, city, grade, seller):
        self.Name = name
        self.City = city
        self.Grade = grade
        self.Seller = seller

    def __repr__(self):
        return f'Id:  {self.id}\n' \
               f'Name:  {self.Name}\n' \
               f'City:  {self.City}\n' \
               f'Grade:  {self.Grade}\n' \
               f'Seller:  {self.Salesperson_id}\n'


try:
    engine = create_engine('sqlite:///q1.db', echo=True)
    print('Connected to SQLite')
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Customers).filter(Customers.Grade > 200).all()
    print(f'Total rows are:   {len(query)}')
    print('Printing each row')
    for item in query:
        print(f'{item}\n')
except Exception as e:
    print(e)
finally:
    session.close()
    print('The SQLite connection is closed')



