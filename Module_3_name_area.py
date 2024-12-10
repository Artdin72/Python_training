# Счётчик вызовов
def count_calls():  # подсчёт вызовов функций
    global calls
    calls +=1
    return calls

def string_info(String):  # подсчёт длины строки и тансформация в верхний и нижний регистры
    global calls
    String = len(String), String.upper(), String.lower()
    count_calls()
    return String

def is_contains(String, List):    # определения присутствия строки в списке
    global calls
    for i in range(len(List)):        # трансформация строки в нижний регистр
        List[i] = List[i].lower()   
    if String.casefold() in List:
        logic = True
    else:
        logic = False
    count_calls()
    return logic

calls = 0
print(string_info('Habanera'))
print(string_info('Subardinaciya'))
print(is_contains('BoR', ['Sam', 'bort', 'Barom', 'B0R']))
print(is_contains('kRot', ['Krokodil', 'kRot.', 'Krota', 'rot']))
print(is_contains('life', ['Piece', 'Word', 'war', 'LIFE', 'death']))
print(calls)
