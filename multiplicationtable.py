def multiplication_table():
    while True:
        Number = int(input("Enter number: "))
        for i in range(1, 11):
            print(Number*i)

        if Number <= 0:
            print("pick positive number")
        
        
        

multiplication_table()
