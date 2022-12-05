import sqlite3
from utility import dictfetchall
connection = sqlite3.connect('viesnica.db')

def reserve():
    with connection as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Istaba")
        visas_istabas = dictfetchall(cur)
    con.close()
    print("Thank you for reserving!")
    print(visas_istabas)


def get_info(izvele):
    if izvele == 1:
        table_name = "Viesis"
        visi_viesi = get_all_data(table_name)


        print("----------------------------------------")
        print("| vards | uzvards | tel_nr| studentsID |")
        print("----------------------------------------")
        for viesi in visi_viesi:
            print("|", viesi["vards"], "|", viesi["uzvards"], "|", viesi["tel_nr"], "|", viesi["studentsID"])
    elif izvele == 2:
        table_name = "Uzturesanas"
        visas_uzturesanas = get_all_data(table_name)

        print("---------------------------------------------------------------")
        print("| ierakstisanas_laiks | izrakstisanas_laiks | istaba | viesis |")
        print("---------------------------------------------------------------")
        for date in visas_uzturesanas:
            print("|", date["ierakstisanas_laiks"], "|", date["izrakstisanas_laiks"], "|", date["istaba"], "|", date["viesis"])
    else:
        table_name = "Istaba"
        visas_istabas = get_all_data(table_name)

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