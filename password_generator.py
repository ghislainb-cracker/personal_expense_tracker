import random
import string

def generate_password(length=12):
    # characters to use
    characters = string.ascii_letters + string.digits + string.punctuation
    # generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to Password Generator")
    length = int(input("Enter password length: "))
    if length < 6:
        print("⚠️ Password length should be at least 6 characters.")
        return
    
    


   
