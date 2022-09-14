# import math
# Use the print function and some spaces to get it looking like the example from the material.
print("Choose either 'investment' or 'bond' from the menu to proceed:")
print(" ")
print("investment     - to calculate the amount of interest you'll earn on interest")
print("bond           - to calculate the amount you'll have to pay on a home loan")
print(" ")
# Get the user's input.
raw_type = input(": ")
# Turn the user's input into lower case so the if function can read it even if it was entered in all caps.
selection = raw_type.lower()
# First if is for when the user selected 'investment' use input to gather the correct date.
if selection == 'investment':
  amount       = int(input("Amount of money to be deposited: "))
  rate_raw     = int(input("Interest rate: "))
  years        = int(input("Number of years: "))
  interest_raw = input("Please enter either 'simple' or 'compound' to get your result: ")
  # Turns 'interest_raw' into lower case so if can read it even if it was entered in all caps.
  interest = interest_raw.lower()
  # Divide the rate the user entered by a 100 to get 2 decimal places for the calculation.
  rate = rate_raw / 100
  # First if is to calculate the simple interest by using the provided formula
  if interest == 'simple':
    answer = amount * (1 + (rate / 100) * years)
    print("Total amount: R{}.00".format(answer))
    print("Interest earned: R{}.00".format(answer - amount))
  # The elif is used to calculate compound interest by using the provided formula.
  elif interest == 'compound':
    answer = int(amount* pow((1 + rate),years))
    print("Total amount: R{}.00".format(answer))
    print("Interest earned: R{}.00".format(answer - amount))
  # else function is used for if the user entered the incorrect word.
  else:
    Print("Invalid input.")
# This elif is used if the user wants to calculate their bond.
elif selection == 'bond':
  value    = int(input("What is the value of the house: R"))
  rate     = int(input("What is the annual interest rate: "))
  months   = int(input("What is the number of months to repay the bond: "))
  interest = rate / months
  answer   = int((interest*value)/(1 - (1+interest)*(-months)))
  # Answer will be printed after it was calculated by the provided formula.
  print("Amount of money to be paid each month: R{}.00".format(answer))
# The else is used for if the user entered the incorrect word at the beginning.
else:
  print("Incorrect input.")
