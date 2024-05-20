# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. 
# The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
# Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

# Input the total change amount
total_change = int(input())

# Define the denominations of each coin
denominations = [('Dollar', 100), ('Quarter', 25), ('Dime', 10), ('Nickel', 5), ('Penny', 1)]

# If the total change is less than or equal to 0, output "No change"
if total_change <= 0:
    print("No change")

# Iterate over the denominations
for coin, value in denominations:
    # Calculate the number of coins needed for this denomination
    num_coins = total_change // value
    # Update the total_change for the next iteration
    total_change %= value
    # Print the number of coins and the coin type
    if num_coins > 0:
        if num_coins == 1:
            print(f"{num_coins} {coin}")
        else:
            print(f"{num_coins} {coin}s")
