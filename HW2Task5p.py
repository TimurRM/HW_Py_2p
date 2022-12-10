# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! 
# Реализовать свой метод

#1
import random
def shaffle_list(my_list):
    list_1 = my_list[:]
    for i in range(len(list_1)):
        index = random.randint(1, len(list_1)-1)
        temp = list_1[i]
        list_1[i] = list_1[index]
        list_1[index] = temp
    return list_1

origin_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_list = shaffle_list(origin_list)
print(f'Original list: {origin_list}')
print(f'Shuffled list: {shuffled_list}')

#2
import datetime
import time

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f'\nOriginal list', my_list)
# print(len(my_list))
for i in range(len(my_list)):
    n = datetime.datetime.now().microsecond % len(my_list)
    # print(datetime.datetime.now().second)
    # print(n)
    shuffled = my_list.pop(int(n))
    # print(shuffled, end= ' ')
    my_list.append(shuffled) 
print('Shuffled list', my_list)






