"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types yes or no
# 2. Process: The program asks up to 10 times and accepts capital letters and extra spaces
# 3. Out: A message about the user's choice and a summary of the attempts
# 4. My stop condition, my attempt limit, my summary: My stop condition is typing yes or no. The maximum is 10 attempts. The summary shows the choice and number of attempts


# Your code below
# Set the maximum attempts and starting values.
attempt_limit = 10
attempts = 0
decision = "The maximum number of attempts was reached."
