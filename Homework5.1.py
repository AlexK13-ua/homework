    # 5.1. Ім'я змінної

import keyword
import string
while True:

    user_input = input("Input you string: ")
    invalid_chars = string.punctuation.replace("_", "")

    valid_chars = True
    if user_input[0].isdigit():
        valid_chars = False
    elif user_input in keyword.kwlist:
        valid_chars = False
    elif any(char.isupper() for char in user_input):
        valid_chars = False
    elif any(char in (invalid_chars + " ") for char in user_input):
        valid_chars = False
    elif "__" in user_input:
        valid_chars = False
    print(valid_chars)

# #################################################


    # user_input = input("Input you string: ")
    #
    # inv_char = (user_input in keyword.kwlist or
    #             (user_input and user_input[0].isdigit()) or
    #             any(char.isupper() for char in user_input) or
    #             any(char in (string.punctuation.replace("_", "") + " ") for char in user_input) or
    #             "__" in user_input)
    # print(not inv_char)

# ##################################################

    # user_input = input("Input your string: ")
    #
    # valid_char = (user_input not in keyword.kwlist and
    #             (user_input == "_" or not user_input[0].isdigit()) and
    #             not any(char.isupper() for char in user_input) and
    #             not any(char in (string.punctuation.replace("_", "") + " ") for char in user_input) and
    #             "__" not in user_input)
    #
    # print(valid_char)

