from options import reserve, get_info, update_info, insert_data, delete_data

print("""Welcome to the menu!      
Please choose an option: 

1.Reserve
2.Update info
3.Get info
4.Insert info
5.Delete info
""")

izvele = int(input())
if izvele == 1:
    reserve()
elif izvele == 2:
    print("""      
    Please choose what you want to update: 

    1.Viesis info
    2.Stay info
    3.Room info
    4.Students info
    """)
    izvele = int(input())
    update_info(izvele)
elif izvele == 3:
    print("""      
    Please choose which info: 

    1.Viesis info
    2.Stay info
    3.Room info
        
    """)
    izvele = int(input())
    get_info(izvele)
elif izvele == 4:
    print("""      
        Choose in what table you want to insert new data: 

        1.Stay data
        2.Room data
        3.Students data
        4.Guest data

        """)
    izvele = int(input())
    insert_data(izvele)
else:
    print("""      
        Choose in what table you want to delete data: 
        1.Stay data
        2.Room data
        3.Students data
        4.Guest data
            """)
    izvele = int(input())
    delete_data(izvele)
