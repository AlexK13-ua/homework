        # 4.1. Перемістити всі нулі до кінця списку

list1 = [0, 1, 2]
num = 0
zeros = list1.count(0)
for i in range(zeros):
    list1.remove(num)
for i in range(zeros):
    list1.append(num)
print(list1)


# list1 = [0, 2, 0, 3, 14, 0, 5, 0]
# zeros = []
# others = []
# for i in list1:
#     if i == 0:
#         zeros.append(i)
#     else:
#         others.append(i)
# rlist = others + zeros
# print(rlist)