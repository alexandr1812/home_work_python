# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

while True:
    try:
        input_data = float(input("Введите число: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

sum = 0

for i in str(input_data):
    if i != '.' and i != ' ':
        sum = sum + int(i)

print(f'-> {sum}')

