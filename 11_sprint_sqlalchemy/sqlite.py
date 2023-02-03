import sqlite3

"""
Create a Python program to use the sqlite database named "q1.db". The query to
the database should display information, as shown in the example below, 
including phrases: about the successful connection, the total number of
records, the actual records, the record of closing the database. From the
table of "customers" to deduce all records for which in a "grade" field of
value more than 200 with sort ordering on id


For example output:

Connected to SQLite
Total rows are:   2
Printing each row
Id:  3022
Name:  Nik Rimando
City:  Madrid
Grade:  1000
Seller:  6001


Id:  3025
Name:  Grem Zusisa
City:  USA
Grade:  2000
Seller:  6002


The SQLite connection is closed
"""


try:
    con = sqlite3.connect('q1.db')
    print('Connected to SQLite')
    with con:
        cur = con.cursor()
        cur.execute('SELECT id, name, city, grade, Salesperson_id Seller '
                    ' FROM customers WHERE grade > 200')
        rows = cur.fetchall()
        names = list(map(lambda x: x[0], cur.description))
        print(f'Total rows are:   {len(rows)}')
        print('Printing each row')
        for row in rows:
            for data in enumerate(row):
                print(f'{names[data[0]].capitalize()}:  {data[1]}')
            print('\n')

except Exception as e:
    print(e)
finally:
    cur.close()
    con.close()
    print('The SQLite connection is closed')

