import sqlite3


def create_database():
    conn = sqlite3.connect(":memory:")
    print("Opened database successfully");

    conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    conn.commit()
    print("Records created successfully");

    list_of_items = (1, 2, 3, 4)
    for i in list_of_items:
        print(i)

    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    conn.close()


def f(x): return x % 3 == 0 or x % 5 == 0



create_database()
x = f(5)
print(x)

filter(f, range(2,25))


# a07eab762373b5e119157eb3ffbfc6f8f7f754f80f01cf6249c997694c85cb1e *pycharm-professional-2016.1.dmg
# a07eab762373b5e119157eb3ffbfc6f8f7f754f80f01cf6249c997694c85cb1e  pycharm-professional-2016.1.dmg
# shasum -a 256 filename