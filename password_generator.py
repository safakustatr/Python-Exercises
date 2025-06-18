import random
import string

def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password
try:
    length = int(input('Please enter a password length: '))
    if length < 5:
        print('Please enter a higher number for more secure password')
    else:
        print('Generated secure password: ' + generate_password(length))
except ValueError:
    print('Please enter a valid number')
