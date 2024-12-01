# Всё не так уж просто
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:          # цикл для числителя со второго индекса
    is_prime = True            # исходное значение
    for j in numbers[1:i-1]:   # цикл для знаменателя
        if i % j != 0:         # если числитель не делится без остатка, то сохраняется исходное значение
            continue           #
        else:
            is_prime = False   # иначе значение меняется на противоположное
    if is_prime == True:
        primes.append(i)       # простое число
    else:
        not_primes.append(i)   # непростое число
print('numbers', numbers)
print('Primers', primes)
print('Not primers',not_primes)