import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///library.db', echo=True)


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,\
    text, select

metadata = MetaData()

authors_table = Table('authors', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String)
                      )

books_table = Table('books', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id'))
                    )

if __name__ == '__main__':

    metadata.create_all(engine)

    insert_stmt = authors_table.insert(bind=engine)

    compiled_stmt = insert_stmt.compile()

    # insert_stmt.execute([{'name': 'John Doo'}, {'name': 'Mari Lee'}])
    metadata.bind = engine

    select_stmt = authors_table.select(authors_table.c.id==2)
    res = select_stmt.execute()
    print('res start')
    print(res)
    print('res end')


    #
    connection = engine.connect()
    select_ = select(authors_table)
    print(connection.execute(select_).fetchall())

