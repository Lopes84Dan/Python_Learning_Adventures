#Statistics are often calculated with varying amounts of input data. 
#Write a program that takes any number of integers as input, and outputs the average and max.
def main():
    # Taking input from the user
    inp = input('Enter numbers with spaces:')

    # Converting the input string to a list of integers
    numbers = [int(i) for i in inp.split()]

    #Calculating the average and max
    average = sum(numbers) / len(numbers)
    maximum = max(numbers)

    # Printing the results
    print(f'Average: {average}')
    print(f'Max: {maximum}')
    
if __name__ == '__main__':
    main()

    