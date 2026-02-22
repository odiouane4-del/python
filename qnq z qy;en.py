import random
import string

def password_generator():
    print("=" * 40)
    print("🔐 Secure Password Generator 🔐")
    print("=" * 40)
    
    while True:
        try:
            length = int(input("\nEnter password length (8-32): "))
            if length < 8 or length > 32:
                print("Please choose a length between 8 and 32.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nSelect password complexity:")
    print("1. Letters only (weak)")
    print("2. Letters and numbers (medium)")
    print("3. Letters, numbers, and symbols (strong)")
    
    while True:
        complexity = input("Enter choice (1-3): ")
        if complexity in ["1", "2", "3"]:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Generate password based on complexity
    if complexity == "1":
        characters = string.ascii_letters
        strength = "Weak"
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
        strength = "Medium"
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        strength = "Strong"
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print("\n" + "=" * 40)
    print(f"Generated Password ({strength}):")
    print(f"🔑 {password}")
    print("=" * 40)
    
    # Ask if user wants another password
    again = input("\nGenerate another password? (yes/no): ").lower()
    if again == "yes":
        password_generator()

# Run the password generator
if __name__ == "__main__":
    password_generator()
    
