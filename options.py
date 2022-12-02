import sqlite3

connection = sqlite3.connect('viesnica.db')

def reserve():
    with connection as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Istaba")
    con.close()
    print("Thank you for reserving!")

reserve()