# Задача 6
# Найти сумму цифр числа.
# We'll use Forward direction tokenizer from Ex5
next_digit = None
sum_total = 0
my_input = input ('Enter the number: ')
int_num = int(my_input)
num_len = len(my_input)
div_num = 10**(num_len-1)
print('Original Number:', int_num)
while num_len > 0:
    next_digit = int_num//div_num
    sum_total += next_digit
    print('Added number', next_digit)
    # calculate next iteration's values
    int_num = int_num-(int_num//div_num*div_num)
    num_len = num_len-1
    div_num = 10**(num_len-1)
print('Sum total of all digits:', sum_total)
