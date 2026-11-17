"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters text that should represent a number.
# 2. Process: The program converts the text to a number and divides 100 by it.
#    It allows 3 attempts. A blank line, invalid text, and zero are handled.
# 3. Out: The program displays the answer or a helpful error message.
# 4. ValueError happens when the input is not a number; ZeroDivisionError
#    happens when the number is zero. They get different messages because
#    they have different causes.
#    I catch them separately so each problem gets the right message.
#    The program allows 3 attempts before stopping safely.


# Your code below
# Check examples:
# - A normal number: displays the answer.
# - 0: says division by zero is not allowed.
# - abc: says the input is not a number.
# - An empty line: says no number was entered.

# This loop gives the user up to three attempts.
for attempt in range(3):
    text = input("Enter a number to divide 100 by: ")

    # Handle an empty line separately.
    if text.strip() == "":
        print("You did not enter anything. Please try again.")
        continue

    # Convert the text to a number.
    try:
        number = float(text)
    except ValueError:
        print("That is not a number. Please try again.")
        continue

    # Divide 100 by the number.
    try:
        result = 100 / number
    except ZeroDivisionError:
        print("You cannot divide by zero. Please try again.")
        continue

    print("100 divided by", number, "is", result)
    break
else:
    print("You used all 3 attempts. The program stopped safely.")