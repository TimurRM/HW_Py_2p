# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

#1
def digitSum(inputed_value):
    summa = 0
    for i in str(inputed_value):
        if i != "." and i != "-":
            summa += int(i)
    return summa

value = input("Введите число: ")
print(f"{value} -> {digitSum(value)}")
  
# # #2
any_value = input("Input value:  ")
summ = 0
numm = 0
for i in any_value:
    try:
        numm = int(i)
    except:
        continue
    summ += numm
print(f'{any_value} -> {summ}')

# #3
value = input('Enter value: ')
digits = int(''.join(list(filter(lambda char: char.isdigit(), value))))


summ = 0
while digits > 0:
    summ += digits % 10
    digits //= 10
print(f'{value} -> {summ}')

#4
def check_num():
    while True:
        try:
            number = float(input(f'Enter number, please: '))
            break
        except:
            print('This is not a number!!! Please, enter digits only!')
        continue
    return number

some_value = check_num()
print(some_value, end=' ')
digit = 0
for i in str(some_value):
    if i != '.' and i != '-':
        digit += int(i)
print(f' -> {digit}')


#5

num = input('Input some value: ')
summa = 0
for i in num:
    if i.isdigit():
        summa += int(i)
print(f'{num} -> {summa}')
