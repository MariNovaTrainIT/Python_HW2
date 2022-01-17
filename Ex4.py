# Задача 4:
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

multiplication = 1
current_number = 1
while current_number <= 10:
    # print('Current Number: ', current_number)
    multiplication *= current_number
    current_number += 1
print('The multiplication of numbers from 1 to 10 is ', multiplication)