        #8.2  Паліндром


def is_palindrome(text):

    text = "".join(l for l in text if l.isdigit() or l.isalpha()).lower()
    return text == text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")