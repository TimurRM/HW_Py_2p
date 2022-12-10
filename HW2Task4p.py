# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

def check_num():
    while True:
        try:
            number = abs(int(input(f'Input number: ')))
            break
        except:
            print('This is not a number!!! Please, enter number!')
        continue
    return number

num = check_num()

def my_str(num):
    my_list = []
    for i in range(- num, num + 1):
        my_list.append(i)
    return my_list

print(my_str(num))

mult_index = list(map(int, input('Input indexes you want to multiply: --> ').split()))
mult = 1
print('Our factors: ', end=':')
for i in mult_index:
    mult *= (my_str(num)[i])
    print(f'[{my_str(num)[i]}]', end=' ')
print(f'\nOutcome: {mult}')
