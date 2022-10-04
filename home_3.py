# 3. Задайте список из n чисел, заполненный по формуле (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {2, 2, 2, 2, 2, 3} sum => 13


while True:
    try:
        num = int(input("Введите число: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")


arr = []
sum = 0
for i in range(1, num + 1):
    formula = int(round((1 + 1 / i) ** i, 0))
    arr.append(formula)
    sum += formula
print(arr, sum)
