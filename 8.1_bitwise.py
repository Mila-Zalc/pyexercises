"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: Permission values represented by bits.
# 2. Process: Combine permissions, check for a permission,
#    add a permission, and remove a permission.
# 3. Out: The permissions and their changes, displayed in binary.
# 4. These permissions are for a marketing campaign:
#    VIEW, EDIT, and PUBLISH.

# Your code below
# Each permission has its own bit.
VIEW = 0b001
EDIT = 0b010
PUBLISH = 0b100

# Combine VIEW and EDIT.
permissions = VIEW | EDIT
print(f"VIEW + EDIT: {permissions:03b}")

# Check whether PUBLISH is included.
publish_check = permissions & PUBLISH
print(f"PUBLISH check: {publish_check:03b}")
print(f"Can publish? {publish_check != 0}")

# Add PUBLISH.
permissions = permissions | PUBLISH
print(f"After adding PUBLISH: {permissions:03b}")

# Remove EDIT.
permissions = permissions & ~EDIT
print(f"After removing EDIT: {permissions:03b}")