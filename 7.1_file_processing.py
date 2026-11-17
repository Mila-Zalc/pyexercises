"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are blank lines
# - Some names have spaces at the beginning of the line
# - Capitalization is inconsistent
# - "van rossum" is a family name made of two words

# 1. In: The program reads names from names.txt, one name per line
# 2. Process, problem by problem: 
# - Skip blank lines
# - Split each line into words to remove extra spaces
# - Capitalize the names consistently and keep "van" lowercase
# - Use the first word as the first name and all remaining words as the family name
# - Sort the names alphabetically by the complete family name
# 3. Out: The program writes the cleaned, sorted names to names_sorted.txt.
# 4. How I decide which word is the last name: For a two-word name, I treat the first word as the first name and the second as the family name. If there are more words, all words after the first are the family name. I sort using those family-name words.


# Your code below
# This function cleans one name.
def clean_name(line):
    words = line.split()

    if len(words) == 0:
        return ""

    first_name = words[0].capitalize()
    family_name_words = []

    for word in words[1:]:
        if word.lower() == "van":
            family_name_words.append("van")
        else:
            family_name_words.append(word.capitalize())

    cleaned_name = " ".join([first_name] + family_name_words)
    return cleaned_name


# This function gets the family name for sorting.
def get_family_name(name):
    words = name.split()
    return " ".join(words[1:]).lower()


# This block reads names.txt without changing the original file.
with open("names.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()


# This block cleans the names, skips blank lines, and sorts the result.
names = []

for line in lines:
    cleaned_name = clean_name(line)

    if cleaned_name != "":
        names.append(cleaned_name)

names.sort(key=get_family_name)


# This block writes the cleaned names to a new file.
with open("names_sorted.txt", "w", encoding="utf-8") as output_file:
    for name in names:
        output_file.write(name + "\n")

print(f"Read {len(lines)} lines and wrote {len(names)} names.")
print("The cleaned names were saved in names_sorted.txt.")