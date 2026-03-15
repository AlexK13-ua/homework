from typing import reveal_type  # 5.2. Модифікувати калькулятор

while True:

    first_number = float(input("Input first number: "))
    second_number = float(input("Input second number: "))
    operator = input("Input your operator (+, -, *, /): ")

    res = "Result: "

    if operator == "+":
        print(res, first_number + second_number)
    elif operator == "-":
        print(res, first_number - second_number)
    elif operator == "*":
        print(res, first_number * second_number)
    elif operator == "/" and second_number == 0:
        print("Error. You can't divide by 0. Try again")
    elif operator == "/":
        print(res, first_number / second_number)


    cont = input("Do you want to continue? Yes (y), No (n): ").lower()
    if cont != "y" and cont != 'y':
        break