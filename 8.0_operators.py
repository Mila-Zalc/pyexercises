"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in? 
    2. What happens to it? 
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: Two text values, "Python" and "python".
# 2. Process: The program compares them with comparison operators,
#    then combines some results with and, or, and not.
# 3. Out: A readable table showing each expression and its True or False result.
# 4. I chose two strings with different capitalization.
#    I was surprised that "Python" < "python" is True.

# Your code below
first_value = "Python"
second_value = "python"

# This list stores each comparison and its result.
results = [
    ("first == second", first_value == second_value),
    ("first != second", first_value != second_value),
    ("first < second", first_value < second_value),
    ("first > second", first_value > second_value),
    ("first <= second", first_value <= second_value),
    ("first >= second", first_value >= second_value),
    (
        "(first == second) and (first < second)",
        (first_value == second_value) and (first_value < second_value)
    ),
    (
        "(first == second) or (first < second)",
        (first_value == second_value) or (first_value < second_value)
    ),
    ("not (first == second)", not (first_value == second_value))
]

# This loop displays the results as a table.
print(f"Comparing {first_value!r} and {second_value!r}")
print(f"{'Expression':<48} | Result")
print("-" * 60)

for expression, result in results:
    print(f"{expression:<48} | {result}")