        # 10.3. Перевірити чи є парним чи ні

def is_even(digit):
    """ Перевірка чи є парним число """


    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

  ########################

        # if digit % 2 == 0:
        #     return True
        # else:
        #     return False


        # if digit % 2 == 0:
        #     return True
        # return False