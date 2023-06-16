import random

def generate_password(full_name):
    # Remove any spaces from the full name
    full_name = full_name.replace(" ", "")
    
    # Select three random letters from the full name
    letters = random.sample(full_name.lower(), 3)
    
    # Generate a random four-digit number
    number = random.randint(1000, 9999)
    
    # Combine the letters and number to form the password
    password = "".join(letters) + str(number)
    
    return password

# Prompt the user for their full name
full_name = input("Please enter your full name: ")

# Generate and print the password
password = generate_password(full_name)
print(password)