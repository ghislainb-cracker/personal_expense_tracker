import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to Password Generator")
    length = int(input("Enter password length: "))
    if length < 6:
        print("⚠️ Password length should be at least 6 characters.")
        return
    password = generate_password(length)
    print(f"\n✅ Your secure password is: {password}")

if __name__ == "__main__":
    main()
