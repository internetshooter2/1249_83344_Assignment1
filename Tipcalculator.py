# Create a program that calculates three options
# for an appropriate tip to leave after a meal at a restaurant.
# Specifications
# The program should calculate
# display the cost of tipping at 15%, 20%, or 25%.
# Assume the user will enter valid data.
# The program should round results to a maximum of two decimal places.

option_A = 0.15 #define 15% option
option_B = 0.20 #define 20% option
option_C = 0.25 #define 25% option

bill_ammount = float(input("Please input your bill ammount before tip: $"))

# allow the user to input a custom bill amount
while True:

    print("Choose a tip Option:")
    print("A: 15%")
    print("B: 20%")
    print("C: 25%")

    #prints the console for what options we give the user

    choice = input("Enter A, B, or C: ").strip().upper()

    #gives the user a choice and allows uppercase or lowercase letters 

    if choice == 'A':
        tip = option_A
        break
    elif choice == 'B':
        tip = option_B
        break
    elif choice == 'C':
        tip = option_C
        break
    else:
        print("Please choose from the provided choices A, B or C.")

# if else statment for a-c and also a error ketching statment at the end for if the user chooses not to read instructions 

tip_ammount = round(bill_ammount * tip, 2)

#mathamatical formula for how to caluclate what the tip amount is and what to tell our user 

print(f"\nThe tip ammount for {choice} would be : ${tip_ammount:.2f}")

#finally we tell our user what the conclusion is and what we have created ":)"
