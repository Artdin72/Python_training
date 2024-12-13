# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(100)
print_params(100, 200)
print_params(100, 200, 300)
print_params(b=25)
print_params(c=[1, 2, 3])

print()

# Распаковка параметров
values_list = [False, (9, 8, 7), 111]
values_dict = {'a':555, 'b':'right', 'c':(1<0)}
print_params(*values_list)
print_params(**values_dict)

print()

# Распаковка + отдельные параметры
values_list_2 = ['Ok', 9]
print_params(*values_list_2, 42)