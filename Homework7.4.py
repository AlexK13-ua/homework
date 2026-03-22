            # 7.4. Пошук спільних елементів

# def common_elements():
#     set_3 = {i for i in range(100) if i % 3 == 0}
#     set_5 = {i for i in range(100) if i % 5 == 0}
#     return set_3 & set_5
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('ОК')

###########################

def common_elements():
    set_3 = {i for i in range(100) if i % 3 == 0}
    set_5 = {i for i in range(100) if i % 5 == 0}
    result = set_3.intersection(set_5)
    return result
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')

###########################
# def common_elements():
#     list_3 = [i for i in range(100) if i % 3 == 0]
#     list_5 = [i for i in range(100) if i % 5 == 0]
#     result = set(list_3).intersection(list_5)
#
#     return result
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('ОК')




