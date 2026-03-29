        # 9.1. Визначити популярність певних слів у тексті

def popular_words (text, words):

    split_text = text.lower().split()
    pop_words_count = {word: split_text.count(word) for word in words}
    return pop_words_count
main_text = '''When I was One I had just begun When I was Two I was nearly new '''
search_words = ['i', 'was', 'three', 'near']
print(popular_words(main_text, search_words))

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')