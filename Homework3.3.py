        #3.3  Розділити один список на два списки

list1 = []
part1 = list1[:]
part2 = list1[:]
result = [part1, part2]
print(result)


# list1 = [1, 2, 3, 4, 5, 6]
# mid_index = len(list1) // 2
# part1 = list1[:mid_index]
# part2 = list1[mid_index:]
# result = [part1, part2]
# print(result)

        ### Option 1
# list1 = [1, 2, 3, 4, 5, 6, 7]
# mid_index = len(list1) // 2
# if len(list1) % 2 != 0:
#     mid_index += 1
#     part1 = list1[:mid_index]
#     part2 = list1[mid_index:]
#     result = [part1, part2]
#     print(result)

        ### Option 2
# list1 = [1, 2, 3, 4, 5, 6, 7]
# mid_index = (len(list1)+1) // 2
# part1 = list1[:mid_index]
# part2 = list1[mid_index:]
# result = [part1, part2]
# print(result)






