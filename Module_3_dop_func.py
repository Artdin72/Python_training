# Раз, два, три, четыре, пять ... Это не всё?
def summ_totall(chaos):
    summ = 0
    if isinstance(chaos, int):            # целое число прибавляем к сумме
        summ += chaos
    elif isinstance(chaos, str):          # считаем количество символов в строке и прибавляем к сумме
        summ += len(chaos)
    elif isinstance(chaos, list):         # к каждому элементу списка применяем саму функцию
        for i in chaos:
            summ += summ_totall(i)
    elif isinstance(chaos, tuple):        # к каждому элементу кортежа применяем саму функцию
        for i in chaos:
            summ += summ_totall(i)
    elif isinstance(chaos, set):          # к каждому элементу множества применяем саму функцию
        for i in chaos:
            summ += summ_totall(i)
    elif isinstance(chaos, dict):         # к каждому элементу пар словаря применяем саму функцию
        for key, value in chaos.items():
            summ += summ_totall(key)
            summ += summ_totall(value)
    return summ

data_structure = [[1, 2, 3], {'a':4, 'b':5}, (6, {'cube':7, 'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = summ_totall(data_structure)
print(result)