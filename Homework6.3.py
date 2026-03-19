        # 6.3 Добуток чисел


while True:
    input_num = int(input("Input you number: "))
    while input_num > 9:
        prod = 1
        for digit in str(input_num):
            prod *= int(digit)
        input_num = prod
    print(input_num)



# input_num = [999, 1000, 423, 33, 25, 1]
# results = []
# for number in input_num:
#     current = number
#
#     while current > 9:
#         product = 1
#
#         for digit in str(current):
#             product *= int(digit)
#             current = product
#             results.append(current)
#     print(current)