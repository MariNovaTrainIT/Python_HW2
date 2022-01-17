# Задача 5:
# Вывести цифры числа на каждой строчке.
'''
# Opposite direction tokenizer
next_digit = None
my_input = input ('Enter the number: ')
int_num = int(my_input)
print('Original Number:', int_num)
print('Digits in opposite direction:')
while int_num > 0:
    next_digit = int_num%10
    print(next_digit)
    int_num = int_num//10
print('Opposite direction digit tokenizer completed.')
'''
# Forward direction tokenizer
next_digit = None
my_input = input ('Enter the number: ')
int_num = int(my_input)
num_len = len(my_input)
div_num = 10**(num_len-1)
print('Original Number:', int_num, 'length:', num_len)
print('Digits:')
while num_len > 0:
    next_digit = int_num//div_num
    print(next_digit)
    # calculate next iteration's values
    int_num = int_num-(int_num//div_num*div_num)
    num_len = num_len-1
    div_num = 10**(num_len-1)
print('Digit tokenizer completed.')
