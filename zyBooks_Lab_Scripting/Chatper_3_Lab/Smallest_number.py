# Write a program whose inputs are three integers, and whose output is the smallest of the three values.


integer_one = int(input('Enter first number:'))
integer_two = int(input('Enter second number:'))
integer_three = int(input('Enter third number:'))

smallest_integer = min(integer_one, integer_two, integer_three)

print(smallest_integer)