# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [3.24, 2.12, 6.17, 1.13, 4]
max_num = lst[0]
min_num = lst[0]
for i in range(len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]
print(f'Максимальный элемент списка: {max_num}')

for i in range(len(lst)):
    if lst[i] < min_num:
        min_num = lst[i]
print(f'Минимальный элемент списка: {min_num}')

result = round((max_num - min_num)%1, 2)
print(f'Разница между дробными частям элементов = {result}')