# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введённых пользователем цифр 5.
qty_fives = 0
loop_iter = 0
my_input = None
while loop_iter < 10:
    loop_iter += 1
    my_input = input ('Enter the next number: ')
    if int(my_input) == 5:
        qty_fives += 1
print('Number of fives is: ', qty_fives)
