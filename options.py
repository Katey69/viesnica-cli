import sqlite3
from utility import dictfetchall
connection = sqlite3.connect('viesnica.db')

def reserve():
    with connection as con:
        cur = con.cursor()
        #cur.execute("SELECT DISTINCT(Istaba.numurs), Istaba.izmers, Istaba.id, Istaba.is_luxury, Istaba.kapacitate FROM istaba LEFT JOIN Uzturesanas ON Istaba.id = Uzturesanas.istaba WHERE datetime() NOT BETWEEN Uzturesanas.ierakstisanas_laiks AND Uzturesanas.izrakstisanas_laiks OR Uzturesanas.istaba IS NULL")
        cur.execute("SELECT * FROM Istaba WHERE Istaba.id NOT IN (SELECT Uzturesanas.istaba FROM Uzturesanas WHERE datetime() BETWEEN Uzturesanas.ierakstisanas_laiks AND Uzturesanas.izrakstisanas_laiks);")
        brivas_istabas = dictfetchall(cur)



    print("-------------------------------------------------")
    print("| id | numurs | izmers | is_luxury | kapacitate |")
    print("-------------------------------------------------")
    if len(brivas_istabas) == 0:
        print("No data")

    else:

        for istaba in brivas_istabas:
            print( "|", istaba["id"], "|", istaba["numurs"], "|", istaba["izmers"], "|", istaba["is_luxury"], "|",
                  istaba["kapacitate"], "|")
        print("Please enter guest info")
        name = input('Name:')
        last_name = input('Last name:')
        number = input('Number:')
        istaba = input('Istaba:')
        print("Student? y/n")
        student = input()
        if student == 'y':
            pers_kods = input('pers_kods:')
            kurss = input('Kurss:')
            cur.execute("INSERT INTO Students(pers_kods, kurss) VALUES (?,?)", (pers_kods, kurss))
            studentsID = cur.lastrowid
            con.commit()

        else:
            studentsID = None
        cur.execute("INSERT INTO Viesis(vards, uzvards, tel_nr, studentsID) VALUES (?,?,?,?)", (name, last_name, number, studentsID))
        viesis = cur.lastrowid
        con.commit()



        start_date = input('Start date:')
        end_date = input('End date:')
        cur.execute("INSERT INTO Uzturesanas(ierakstisanas_laiks, izrakstisanas_laiks, istaba, viesis) VALUES (?,?,?,?)", (start_date, end_date, istaba, viesis))

        con.commit()
        print('Data entered successfully.')



def get_info(izvele):
    if izvele == 1:
        print("""      
        Please choose which info: 

        1.All guests
        2.By nosaukums
        
        """)
        izvele1 = int(input())
        if izvele1 == 1:

            table_name = "Viesis"
            visi_viesi = get_all_data(table_name)


            print("----------------------------------------")
            print("| vards | uzvards | tel_nr| studentsID |")
            print("----------------------------------------")
            for viesi in visi_viesi:
                print("|", viesi["vards"], "|", viesi["uzvards"], "|", viesi["tel_nr"], "|", viesi["studentsID"])
        else:
            print("Please write name:")
            nosaukums = input()
            table_name = "Viesis"
            with connection as con:
                cur = con.cursor()
                cur.execute("SELECT Viesis.vards, Viesis.uzvards, Viesis.tel_nr, Viesis.studentsID, Students.pers_kods, Students.kurss FROM {name} LEFT JOIN Students ON Students.id = Viesis.studentsID WHERE vards = '{nosaukums}' ".format(name=table_name, nosaukums=nosaukums))
                result = dictfetchall(cur)
            con.close()
            print("------------------------------------------------------------")
            print("| vards | uzvards | tel_nr| studentsID | pers_kods | kurss |")
            print("------------------------------------------------------------")

            if len(result) == 0:
                print("No data")
            else:
                viesi = result[0]
                print("|", viesi["vards"], "|", viesi["uzvards"], "|", viesi["tel_nr"], "|", viesi["studentsID"], "|", viesi["pers_kods"], "|", viesi["kurss"])



    elif izvele == 2:
        table_name = "Uzturesanas"
        visas_uzturesanas = get_all_data(table_name)

        print("---------------------------------------------------------------")
        print("| ierakstisanas_laiks | izrakstisanas_laiks | istaba | viesis |")
        print("---------------------------------------------------------------")
        for date in visas_uzturesanas:
            print("|", date["ierakstisanas_laiks"], "|", date["izrakstisanas_laiks"], "|", date["istaba"], "|", date["viesis"])

    elif izvele == 3:
        print("""      
    Please choose which info: 

    1.All room
    2.By type
    """)
        izvele1 = int(input())
        get_room_info(izvele1)

    else:
        table_name = "Students"
        visi_studenti = get_all_data(table_name)

        print("---------------------")
        print("| pers_kods | kurss |")
        print("---------------------")
        for studenti in visi_studenti:
                print("|", studenti["pers_kods"], "|", studenti["kurss"])

def get_room_info(izvele1):
    table_name = "Istaba"
    if izvele1 == 1:
        visas_istabas = get_all_data(table_name)

        print("--------------------------------------------")
        print("| numurs | izmers | is_luxury | kapacitate |")
        print("--------------------------------------------")
        for istaba in visas_istabas:
                    print("|", istaba["numurs"], "|", istaba["izmers"], "|", istaba["is_luxury"], "|",
                        istaba["kapacitate"])
    else:
        print("Please enter minimum capacity")
        capacity = int(input())
        print("Please enter minimum size")
        size = int(input())
        print("Please enter if luxury y/n?")
        luxury = input()
        if luxury == "y":
            luxury = 1
        else:
            luxury = 0


        with connection as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM {name} WHERE kapacitate > {capacity} AND izmers > {size} AND is_luxury = {luxury}".format(name=table_name, capacity = capacity, size = size, luxury = luxury))
            visas_istabas = dictfetchall(cur)
        con.close()
        print("--------------------------------------------")
        print("| numurs | izmers | is_luxury | kapacitate |")
        print("--------------------------------------------")
        for istaba in visas_istabas:
            print("|", istaba["numurs"], "|", istaba["izmers"], "|", istaba["is_luxury"], "|",
                  istaba["kapacitate"])




def get_all_data(table_name):
    with connection as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM {name}".format(name=table_name))
        visas_istabas = dictfetchall(cur)
    con.close()
    return visas_istabas

def update_info(izvele):
    if izvele == 1:
        table_name = "Viesis"
        visi_viesi = get_all_data(table_name)
        connection = sqlite3.connect('viesnica.db')
        print("---------------------------------------------")
        print("| id | vards | uzvards | tel_nr| studentsID |")
        print("---------------------------------------------")
        for viesi in visi_viesi :
            print("|", viesi["id"], "|", viesi["vards"], "|", viesi["uzvards"], "|", viesi["tel_nr"], "|", viesi["studentsID"])
        print("Please write id:")
        id = int(input())

        print("""      
        Choose what you want to update: 

    1.Name
    2.Last name
    3.Number
    
    """)

        izvele1 = int(input())
        if izvele1 == 1:
            name = input("New name:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Viesis SET vards = '{name}' WHERE id = '{id}'".format(name = name, id = id))
            con.close()

        elif izvele1 == 2:
            last_name = input("New last name:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Viesis SET uzvards = '{last_name}' WHERE id = '{id}'".format(last_name = last_name, id = id))
            con.close()

        else:
            number = input("New number:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Viesis SET tel_nr = '{number}' WHERE id = '{id}'".format(number =  number, id = id))
            con.close()
    if izvele ==  2:
        table_name = "Uzturesanas"
        visas_uzturesanas = get_all_data(table_name)
        connection = sqlite3.connect('viesnica.db')
        print("---------------------------------------------------------------")
        print("| id | ierakstisanas_laiks | izrakstisanas_laiks | istaba | viesis |")
        print("---------------------------------------------------------------")
        for date in visas_uzturesanas:
            print("|", date["id"], "|", date["ierakstisanas_laiks"], "|", date["izrakstisanas_laiks"], "|", date["istaba"], "|",
                  date["viesis"])
        print("Please enter id:")
        id = int(input())
        print("""      
            Choose what you want to update: 

            1.Start date
            2.End date
            """)
        izvele2 = int(input())
        if izvele2 == 1:
            start_date = input("Enter new start date:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Uzturesanas SET ierakstisanas_laiks = '{start_date}' WHERE id = '{id}'".format(start_date = start_date, id = id))
            con.close()
        else:
            end_date = input("Enter new end date:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Uzturesanas SET izrakstisanas_laiks = '{end_date}' WHERE id = '{id}'".format(end_date = end_date, id = id))
            con.close()

    if izvele == 3:
        table_name = "Istaba"
        visas_istabas = get_all_data(table_name)
        connection = sqlite3.connect('viesnica.db')
        print("--------------------------------------------")
        print("| id | numurs | izmers | is_luxury | kapacitate |")
        print("--------------------------------------------")
        for istaba in visas_istabas:
            print("|", istaba["id"], "|", istaba["numurs"], "|", istaba["izmers"], "|", istaba["is_luxury"], "|",
                  istaba["kapacitate"])
        print("Please enter id:")
        id = int(input())
        print("""      
            Choose what you want to update: 
                1.Room number
                2.Size
                3.Luxury status
                4.Capacity
                """)
        izvele3 = int(input())
        if izvele3 == 1:
            room_nr = input("Enter new room nr:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Istaba SET numurs = '{room_nr}' WHERE id = '{id}'".format(room_nr = room_nr, id = id))
            con.close()
        elif izvele3 == 2:
            size = input("Enter the new size:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Istaba SET izmers = '{size}' WHERE id = '{id}'".format(size = size, id = id))
            con.close()
        elif izvele3 == 3:
            luxury = input("Enter if luxury (1 or 0):")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Istaba SET is_luxury = '{luxury}' WHERE id = '{id}'".format(luxury = luxury, id = id))
            con.close()
        else:
            kapacitate = input("Enter new capacity:")
            with connection as con:
                cur = con.cursor()
                cur.execute("UPDATE Istaba SET kapacitate = '{kapacitate}' WHERE id = '{id}'".format(kapacitate = kapacitate, id = id))
            con.close()