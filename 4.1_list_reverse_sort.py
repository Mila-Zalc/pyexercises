"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original list of marketing channels from Exercise 4.0
# 2. Process: The program displays the list in four different orders
# 3. Out: The four orders, followed by the unchanged original list
# 4. My four orders, and which ones modify the original:  My four orders are original, alphabetical, reverse alphabetical, and backwards
# sort() and reverse() change the copies. The original list stays unchanged.


# Your code below
# Use the same original list as in Exercise 4.0.
channels = ["email", "instagram", "facebook", "tiktok", "youtube", "google ads", "events", "direct mail"]

# Make a sorted copy and a backwards copy.
alphabetical = channels.copy()
alphabetical.sort()
backwards = channels.copy()
backwards.reverse()

# Display the list in four different orders.
print("Original order:", channels)
print("Alphabetical:", alphabetical)
print("Reverse alphabetical:", sorted(channels, reverse=True))
print("Backwards:", backwards)

# Display the original list again to prove it stayed unchanged.
print("Original list at the end:", channels)
