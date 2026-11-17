"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: The user enters a campaign name, a promo code, and a discount percentage.
# 2. Process: The program checks each value against its rule.
#    It saves the values only when all three are accepted.
# 3. Out: The program shows which values are invalid, or confirms that they were saved.
# 4. My fields and rules:
#    - Campaign name: English letters only, with no spaces.
#    - Promo code: exactly two uppercase letters followed by three digits.
#    - Discount: a whole number from 1 to 99, without a percent sign.

# Your code below
import re

# ^ means start; [A-Za-z] means one English letter; + means one or more; $ means end.
campaign_pattern = r"^[A-Za-z]+$"

# ^ means start; [A-Z] means an uppercase letter; {2} means exactly two;
# \d means a digit; {3} means exactly three; $ means end.
promo_pattern = r"^[A-Z]{2}\d{3}$"

# ^ means start; [1-9] means a digit from 1 to 9;
# [0-9]? means an optional second digit; $ means end.
# This accepts whole numbers from 1 to 99.
discount_pattern = r"^[1-9][0-9]?$"

campaign_name = input("Campaign name: ").strip()
promo_code = input("Promo code: ").strip()
discount = input("Discount percentage (1-99): ").strip()

campaign_is_valid = re.fullmatch(campaign_pattern, campaign_name) is not None
promo_is_valid = re.fullmatch(promo_pattern, promo_code) is not None
discount_is_valid = re.fullmatch(discount_pattern, discount) is not None

if not campaign_is_valid:
    print("Campaign name must contain English letters only, with no spaces.")

if not promo_is_valid:
    print("Promo code must have two uppercase letters followed by three digits.")

if not discount_is_valid:
    print("Discount must be a whole number from 1 to 99.")

if campaign_is_valid and promo_is_valid and discount_is_valid:
    with open("campaign_data.txt", "a", encoding="utf-8") as file:
        file.write(f"{campaign_name},{promo_code},{discount}\n")

    print("All three values are valid and have been saved.")
else:
    print("Nothing was saved because at least one value was invalid.")