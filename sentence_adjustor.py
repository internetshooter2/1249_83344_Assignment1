
# Write a Python program that prompts the user to enter a sentence. 
# The program should then perform the following operations:
# Print the original sentence.
# Calculate and print the length of the sentence.
# Convert the sentence to uppercase and print it.
# Convert the sentence to lowercase and print it.
# Split the sentence into words and print each word on a separate line.
# Join the words back into a single string, 
# separated by spaces, and print it.
# Ask the user to enter a substring to search for.
# Check if the sentence starts with the provided
# substring and print the result.
# Check if the sentence ends with the provided substring and print 
# the result.
# The program should handle any errors gracefully 
# and provide clear instructions and prompts to the user.



plate = input("Please type something here: ")
while not plate.strip(): # Make sure that user actually provided an input
    print("The input cannot be empty :|")
    plate = input("Please try again: ")

if plate.isdigit():
    print("\nNote: You entered a numeric value.")
    exit()  # I dont like digits :| my life is only words

print("Original Sentence:")
print(plate)  #legit just prints the users input

print("Legnth of the Sentence:")
print(len(plate)) #uses len to print legnth returns as an int

upper_case = plate.upper()
print("Uppercase Sentence:")
print(upper_case)  #turns all the caracter in sentence to uppercase

lower_case = plate.lower()
print("Lowercase Sentence:")
print(lower_case) #turns all the caracter in sentence to lowercase

words = plate.split()
print("Words in the Sentence:")
print("\n".join(words)) #Splits all scentence into words and prints on individual lines

joined = ' '.join(words)
print("Joined Sentence:")
print(joined) #join the words back into a single string sepreated by spaces and prints it (kinda cheated the system here)

substring = input("Please enter a substring to search for: ")

starts_with = plate.startswith(substring)
print(f"Does the sentence start with '{substring}'? {starts_with}")

ends_with = plate.endswith(substring)
print(f"Does the sentence end with '{substring}'? {ends_with}")
