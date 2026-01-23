import random
letters = ['a','b','c','d',
'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '£', '$', '%', '&', '*', '(', ')', '@', '#', '+']
 
print ("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like ? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

# Easy Level 
#password = ""

##nr_letters = 4 suppose
#for char in range (0, nr_letters):
    ##random_char = random.choice(letters)
    ##random_choice is a function
    ##print(random_char)
    ##password = password + random_char
    #password += random.choice(letters)
    ##print(password)

#for char in range (0, nr_numbers):
#    password += random.choice(numbers)

#for char in range (0, nr_symbols):
#    password += random.choice(symbols)
    
#print (password)

#Hard Level
password_list = []

#nr_letters = 4 suppose
for char in range (0, nr_letters):
    #random_char = random.choice(letters)
    #random_choice is a function
    #print(random_char)
    #password = password + random_char
    password_list += random.choice(letters)
    #print(password)

for char in range (0, nr_numbers):
    password_list += random.choice(numbers)

for char in range (0, nr_symbols):
    password_list += random.choice(symbols)
    
#print (password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
    
print (f"Your password is :{password}" )

