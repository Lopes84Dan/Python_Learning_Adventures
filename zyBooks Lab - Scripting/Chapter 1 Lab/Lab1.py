#Write a program using integers user_num and x as input, and output user_num divided by x three times

#Note: In Python 3, integer division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).

user_num = int(input('Enter number:'))

divide_num = int(input('Enter dividing number:'))

#This will divide the numbers three times
first = user_num // divide_num
second = first // divide_num
third = second // divide_num

print(first, second, third)