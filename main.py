import sqlite3

con = sqlite3.connect('viesnica.db')

cur = con.cursor()


cur.execute("""   
        INSERT INTO Students VALUES(9,"123456-88902","TPK21");
         """)

con.commit()

con.close()




