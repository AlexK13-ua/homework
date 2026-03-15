        # 5.3. hashtag

import string

entry = str(input("Input your string: "))

rem_symbols = str.maketrans('', '', string.punctuation)
clean_entry = entry.translate(rem_symbols)
words = clean_entry.title().split()
hashtag = "#" + "".join(words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)






