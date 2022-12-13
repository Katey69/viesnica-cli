from options import reserve, get_info, update_info

print("""Welcome to the menu!      
Please choose an option: 

1.Reserve
2.Update info
3.Get info
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
    """)
    izvele = int(input())
    update_info(izvele)
elif izvele == 3:
    print("""      
    Please choose which info: 

    1.Viesis info
    2.Stay info
    3.Room info
    4.Students info
    """)
    izvele = int(input())
    get_info(izvele)

