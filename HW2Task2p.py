# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def check_num():
    while True:
        try:
            number = int(input(f'Input number: '))
            break
        except:
            print('This is not a number!!! Please, enter number!')
        continue
    return number

num = check_num()

my_array = []
mult = 1
for i in range(1, num + 1):
    mult *= i
    my_array.append(mult)

print(my_array)

  


