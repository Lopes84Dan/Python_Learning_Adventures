#Warm up: Variables, input, and type conversion
#(1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into separate variables. Then, output those four values on a single line separated by a space. (Submit for 2 points).

#(2) Extend to also output in reverse. (Submit for 1 point, so 3 points total).

#(3) Extend to convert the integer to a character by using the 'chr()' function, and output that character. (Submit for 2 points, so 5 points total).

integer = int(input('Enter integer (32 - 126):\n'))
float_num = float(input('Enter float:\n'))
character = input('Enter character:\n')
string = input('Enter string:\n')

print(integer, float_num, character, string)
print(string, character, float_num, integer)
print(integer, 'converted to a character is', chr(integer))