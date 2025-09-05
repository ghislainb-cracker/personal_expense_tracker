import random
import string

def generate_password(length=12):
    # characters to use
    characters = string.ascii_letters + string.digits + string.punctuation
    # generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    


    
    
    
        
        
    
    


   
