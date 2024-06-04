import random

def get_user_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            user_input = int(input(prompt))
            if (min_val is not None and user_input < min_val) or (max_val is not None and user_input > max_val):
                print(f"Please enter a number between {min_val} and {max_val}")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    min_val = get_user_input("Enter the lower bound: ")
    while True:
        max_val = get_user_input("Enter the upper bound: ")
        if max_val > min_val:
            break
        else:
            print("Upper bound must be greater than lower bound. Please try again.")
    
    secret_number = random.randint(min_val, max_val)
    guess_count = 0
    
    while True:
        guess = get_user_input(f"Guess a number between {min_val} and {max_val}: ", min_val, max_val)
        guess_count += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {guess_count} guesses.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    main()
