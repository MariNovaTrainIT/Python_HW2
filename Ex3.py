# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)
'''
# Option 1:
sum_total = 0
for current_number in range(1,102):
	sum_total += current_number
print('The sum of numbers from 1 to 101 is ', sum_total)

# Option 2:
'''
sum_total = 0
current_number = 1
while current_number < 102:
	sum_total += current_number
	current_number += 1
print('The sum of numbers from 1 to 101 is ', sum_total)
print('The control calculation (1+101)*50+51 = ', (1+101)*50+51)
