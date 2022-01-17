# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?
# We'll use Forward direction tokenizer from Ex5
next_digit = None
num_of_fives = 0
my_input = input ('Enter the number: ')
int_num = int(my_input)
num_len = len(my_input)
div_num = 10**(num_len-1)
# print('Original Number:', int_num)
while num_len > 0:
    next_digit = int_num//div_num
    if next_digit == 5:
        num_of_fives += 1
        print('There is number 5 in entered number!')
        break
    # calculate next iteration's values
    int_num = int_num-(int_num//div_num*div_num)
    num_len = num_len-1
    div_num = 10**(num_len-1)
if num_of_fives == 0:
    print('There is no number 5 in entered number!')