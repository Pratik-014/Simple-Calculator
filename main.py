try:
    a = int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("what kind of operation do you want to perform? \nPress + for addition \n- for subtraction \n* for multiplication \n/ for division")
    
    operation = input("Enter the operation: ")
    match operation:
        case '+':
            print(f"The result of {a} + {b} is: {a + b}")
        case '-':
            print(f"The result of {a} - {b} is: {a - b}")
        case '*':
            print(f"The result of {a} * {b} is: {a * b}")
        case '/':
            if b != 0:
                print(f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _: 
            print("Invalid operation. Please enter +, -, *, or /.")
                                  
    
except Exception as e: 
    print("Enter a valid number of a and b")   