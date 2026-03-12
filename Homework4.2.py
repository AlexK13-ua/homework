    # 4.2 Знайти суму елементів із парними індексами

list1 = [0, 1, 7, 2, 4, 8]
if len(list1) == 0:
    print(list1)
else:
    even_sum = sum(list1[::2])
    last_el = list1[-1]
    print(even_sum * last_el)

# list1 = []
# if len(list1) == 0:
#     print(list1)
# else:
#     even_sum = 0
#     for i in range(0, len(list1), 2):
#         even_sum += list1[i]
#     last_el = list1[-1]
#     print(even_sum * last_el)