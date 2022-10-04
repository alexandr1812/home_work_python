# Напишите програму, которая на вход принимает два числа.
# Задайте список N элементов, заполненный числами в промежутке[-N, N]
# Найдите произведение элементов на указанных позициях (не индексах)

while True:
    try:
        n = int(input("Введите число: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


array = list(range(-n, n + 1))
pos_1 = int(input('Первая позиция: '))
pos_2 = int(input('Вторая позиция: '))

for i in range(len(array)):
    faind_pos = array[pos_1 - 1] * array[pos_2 - 1] 

print(f'{array} \nПроизведение позиций => {faind_pos}\n')

