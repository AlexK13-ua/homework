    # 3.1 Калькулятор

while True:    #
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

        ###

# while True:
#     first_number = float(input("Input first number: "))
#     second_number = float(input("Input second number: "))
#     operator = input("Input your operator (+, -, *, /): ")
#
#     res = "Result: "
#
#     if operator == "+":
#         sum_res = first_number + second_number
#         print(res, sum_res)
#     elif operator == "-":
#         sub_res = first_number - second_number
#         print(res, sub_res)
#     elif operator == "*":
#         mul_res = first_number * second_number
#         print(res, mul_res)
#     elif operator == "/" and second_number == 0:
#         print("Error. You can't divide by 0. Try again")
#     elif operator == "/":
#         div_res = first_number / second_number
#         print(res, div_res)