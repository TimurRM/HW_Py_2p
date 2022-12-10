# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06


def my_list(num): 
    mainList = []
    for i in range(1, num + 1):
        mainList.append(round((1+1/i)**i,2))
    return mainList

number = int(input('Введите число: '))
result = my_list(number)

def sumOfMylist(result):
    summ = 0
    for i in range(len(result)):
        summ += result[i]
    return summ
 


print(f'My list: {my_list(number)}')
print(f'Summ: {sumOfMylist(result)}')