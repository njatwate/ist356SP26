# Code Challenge 1-1-2
'''
Let' write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
'''
#Input
amount = float(input("Enter the amount of the check: "))
tip_percent = float(input("Enter the tip percentage (e.g., 0.15 for 15%): "))
num_diners = int(input("Enter the number of diners: "))

# Calculate the total amount with tip.
tip_amount = amount * tip_percent
total_amount = amount + tip_amount

# Calculate what each person owes
amount_per_person = total_amount / num_diners

# Output the results, formatted to two decimal places for currency.
print(f"Total amount: ${amount:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount with tip: ${total_amount:.2f}")
print(f"Each diner owes: ${amount_per_person:.2f}")


