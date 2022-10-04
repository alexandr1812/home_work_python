# Реализуйте алгоритм премешивания списка. Без применения функции shuffle из модуля random


import random

while True:
    try:
        n = int(input("Введите число: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")


array = []

for i in range(-n, n + 1):
    array.append(i)

print(array)
mix = random.sample(array, k = (len(array)))
print(mix)
