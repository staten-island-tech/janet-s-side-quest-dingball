def multiplication_table():
    while True:
        user_input = input("Enter a number or type exit to exit: ")
        if user_input == ('exit'):
            break

        Number = int(user_input)
        if Number == 0:
            print("pick different number")
        elif Number >0:
            for i in range(1, 11):
                print(Number*i)

multiplication_table()
