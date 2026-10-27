"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A whole number typed by the user
# 2. Process: Check each number from 1 to N
# 3. Out: Say whether each number is odd or even
# 4. What happens on 0, on a negative number, on a very large number:For 0 or a negative number, show a message asking for a positive number
# For 5000 or more, show a message that the number is too large

# Ask the user for a number
n = int(input("Type a whole number: "))

# Show a message if the number is outside the accepted range
if n <= 0:
    print("Please type a positive number")
elif n >= 5000:
    print("That number is too large")
else:
    # Check each number from 1 to N
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")