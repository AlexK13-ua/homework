        # 3.2. Перемістити елемент у списку

        ####### Option one


list1 = [1, 2, 3]

if len(list1) == 0:
    print(list1)
elif len(list1) > 0:
        element_replacement = list1.pop()
        list1.insert(0, element_replacement)
        print(list1)

        ####### Option two


# list1 = [1, 2, 3]
# if len(list1) == 0:
#     print(list1)
# elif len(list1) > 0:
#     list1.insert(0, list1[-1])
#     list1.pop()
#     print(list1)