# Однокоренные
def single_root_words(root_word, *other_words): # поиск слов по корню и поиск корней в слове
    same_words = []
    root_word.lower()
    for i in range(len(other_words)):
        if len(root_word) >= len(other_words[i]) and other_words[i].lower() in root_word: # обязательное слово длиннее или ==
            same_words.append(other_words[i]) # добавляем в отбор
        elif len(root_word) < len(other_words[i]) and root_word in other_words[i].lower(): # обязательное слово короче
            same_words.append(other_words[i]) # добавляем в отбор
        else:
            continue
    return same_words

result1 = single_root_words('subordinaciya', 'Aciy', 'borod', 'SuB')
result2 = single_root_words('kot', 'koTovasiya', 'kaotok', 'lokoToK', 'roffKOTal')

print(result1)
print(result2)