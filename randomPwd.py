import random
import string

print("Welcome to the Random Password Generator!")

# Function to generate a password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Ask user for desired password length
while True:
    try:
        length = int(input("Enter the desired length for your password (minimum 8): "))
        if length < 8:
            print("Password length should be at least 8. Try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Generate and display the password
password = generate_password(length)
print("\nYour random password is:")
print(f"🔒 {password} 🔒")
