import re

password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&*!]).{8,}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")