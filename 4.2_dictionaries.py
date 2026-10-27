"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A customer's name, age, city, email, and status
# 2. Process: Store the details, read and change a value, check a missing field, and remove a field
# 3. Out: The customer's details and a message for the missing field
# 4. My object, my five fields, and why those: My object is a customer. I chose these fields because they describe and help contact a customer


# Your code below
# Set the customer's details
name = "Alex"
age = 30
city = "Paris"
email = "alex@example.com"
status = "New"

# Put the details in a dictionary.
customer = { 
            "name": name,
            "age": age,
            "city": city,
            "email": email,
            "status": status
}

# Display the dictionary and read the customer's name.
print("The dictionary is:", customer)
print("Customer name:", customer["name"])

# Change the customer's status
customer["status"] = "Contacted"

# Ask for a field that is missing without causing an error
print("Phone:", customer.get("phone", "Field not found"))

# Remove the city and display every remaining field with its value
customer.pop("city")
for field, value in customer.items():
    print(field, ":", value)