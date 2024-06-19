# Write a program that gets a list of integers from input,
# and outputs non-negative integers in ascending order (lowest to highest).

# For coding simplicity, follow every output value by a space.
# Do not end with newline.

def main():
    # Taking input from the user
    inp = input('Enter numbers with spaces: ')

    # Converting the input string into a list of integers
    numbers = [int(num) for num in inp.split()]

    # Sorting the list of integers in ascending order
    sorted_numbers = sorted(num for num in numbers if num >= 0)

    # Printing each non-negative integer followed by a space
    for num in sorted_numbers:
        print(num, end=' ')

if __name__ == '__main__':
    main()