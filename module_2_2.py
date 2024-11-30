number_1 = int(float(input('Введите первое целое число :'))) #вводим первое число
number_2 = int(float(input('Введите второе целое число :'))) #вводим второе число
number_3 = int(float(input('Введите третье целое число :'))) #вводим третье число
if number_1 == number_2 and number_2 == number_3: #условие равенства всех трёх чисел, как менее вероятное
    print('3. Все три числа равны')
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3: #условие равенства двух из трёх чисел
    print('2. Два числа из трёх равны')
else:
    print('0. Числа не равны')