"""
Jalen Banks
Feb 3, 2026
Lab 3: Conditional statements and loops in Python
"""
print("\n--- Example 1: Conditional statements and loops in Python ---\n")
# Conditional statements control the flow of the program

age = 21

if age >= 21:
    print("You are an adult")
elif age >= 12:
    print("You are a teen")
elif age > 0:
    print("You are a child")
else:
    print("Unable to read age")
print("\n--- Example 2: For loop ---\n")
# For loop as a counter to print from 9 to 1, step 1

for n in range(9,0,-1):
    print(n)

# for the loop in a list
numbers=[3,6,1,-8,9,-5]
for m in numbers:
    print(m)

print("\n--- Example 3: for loop in a list ---\n")
numbers=[3,6,1,-8,9,-5]
count_negative=0
for m in numbers:
    if m<0:
        count_negative+=1
else:
    print(f"there is/are {count_negative} negative numbers")
# for-else, the else statement will run only after the completion of all iterations of the for loop

print("\n--- End of program ---\n")

print("\n--- Example 4: While loop as a counter ---\n")
# While loop as a counter to print from -3 to 5,inclusive, step 1 of 2, output ---> -3 -1 1 3 5
x = -3
while x <= 5:
    print(x)
    x +=2
print("\n--- Example 5: While loop to validate an input ---\n")
# program collects a number from a user and print if the number is even or odd
# afte it, the program will ask the user if another number will be tested
# if the user type 'y' or 'Y' then the program will repeat
# if the user types any other character that is not 'y' or 'Y', the program will end
decision = 'y'
user_number = 0 

while True:
    user_number=int(input("Please enter an number: "))
    if user_number % 2 == 0 and user_number != 0:
        print(f"The number {user_number} is even")
    elif user_number == 0:
        print(f"The number {user_number} is zero")
    else:
        print(f"The number {user_number} is odd")
    decision_user=input("Do you want to test another number? (y/n): ")
    if not (decision_user == 'y' or decision_user == 'Y'):
        break
print("\n--- EXCERCISE 1: Validate a number between 1 and 9 ---\n")
while True:
    user_number=int(input("Please enter an number: "))
    if user_number >1 and user_number <9:
        print(f"Good Job! The number {user_number} is between 1 and 9")

        break
print("\n--- EXCERCISE 2: Guess a number with 3 attempts ---\n")
user_number=7
attempts=0
while attempts < 3:
    user_number=int(input("Please enter an number: "))
    if user_number ==7:
        print(f"Good Job! You guessed the correct number {user_number}")
    elif user_number !=7:
        print(f"Sorry! The number {user_number} is incorrect. Try again")
    user_number=int(input("Please enter an number: "))
    attempts += 1
    print(f"Sorry! The number {user_number} is incorrect. Try again")
    user_number=int(input("Please enter an number: "))
    break