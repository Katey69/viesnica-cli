from options import reserve,get_info

print("""Welcome to the menu!      
Please choose an option: 

1.Reserve
2.Update info
3.Get info
""")

izvele = int(input())
if izvele == 1:
    reserve()
elif izvele == 3:
    print("""      
    Please choose which info: 

    1.Viesis info
    2.Stay info
    3.Room info
    """)
    izvele = int(input())
    get_info(izvele)

