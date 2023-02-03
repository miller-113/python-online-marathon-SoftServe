from sqlalchemy import text, create_engine

engine = create_engine('sqlite:///library4.db')

with engine.connect() as conn:
    result = conn.execute(text("select * from books"))
    print(result.all())
