import random

chars = 'abcdefghijklmopqrstuvwxyz1234567890!@£$%^&*'

number = input('number of characters - ')
number = int(number)

length = input('length of characters - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)