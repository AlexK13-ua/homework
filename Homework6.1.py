        # 6.1. Діапазон букв

import string

while True:

    user_input = (input("Input your letters range: "))
    symbols = string.ascii_letters
    first_sym, last_sym = user_input.split("-")
    start_sym = symbols.find(first_sym)
    end_sym = symbols.find(last_sym)
    if  start_sym <= end_sym:
        result = symbols[start_sym : end_sym + 1]
    else:
        result = symbols[start_sym : end_sym  -1 : -1] if end_sym > 0 else symbols[start_sym : : -1]
    print(result)
