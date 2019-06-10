# Concatenation and integer to string
age = 22
print("This is my " + str(age) + "nd birthday!")

# String to titlecase
myFullName = "justin river ng"
print(myFullName.title())

# String to uppercase
yelling = "stop"
print(yelling.upper())

# Get rid of left spaces, then get rid of extra spaces on both sides
chocolate = "\tchocolate\t"
print(chocolate)
print(chocolate.lstrip())
print(chocolate.strip())

# Access the 2nd to last item on a list
names = ['Jeffrey', 'Josh', 'Justin', 'James']
print(names[-2])

# Add to a list
names = ['Jeffrey', 'Josh', 'Justin', 'James']
names.append('Jacob')
print(names)

# Insert in a list at index 3
names = ['Jeffrey', 'Josh', 'Justin', 'James']
names.insert(3, 'Jean')
print(names)

# Delete an item from a list
names = ['Jeffrey', 'Josh', 'Justin', 'James']
del names[0]
print(names)

# Delete an item from a list using pop
names = ['Jeffrey', 'Josh', 'Justin', 'James']
myName = names.pop(2)
print(names)
print(myName)

# Remove an item from a list by value
names = ['Jeffrey', 'Josh', 'Justin', 'James']
names.remove('Justin')
print(names)

# Sort a list by reverse alphabetical order permanently
fruit = ['kiwi', 'banana', 'apple', 'orange']
fruit.sort(reverse=True)
print(fruit)

# Sort a list in alphabetical order temporarily
fruit = ['kiwi', 'banana', 'apple', 'orange']
print(sorted(fruit))

# Printing a list in reverse order
flavors = ['chocolate', 'vanilla', 'strawberry']
flavors.reverse()
print(flavors)

# Finding the length of a list
flavors = ['chocolate', 'vanilla', 'strawberry']
flavorsLength = len(flavors)
print(flavorsLength)

# Loops
names = ['Jeffrey', 'Josh', 'Justin', 'James']
for person in names:
    print('Hello, ' + person + '\n')  # Must indent the line of code that is to be executed
print('Did I miss anyone?')  # at each iteration of code

# Create a list of even numbers between 2 and 10
evens = list(range(2, 11, 2))
print(evens)

# Find min, max, and sum of a list of numbers
random_numbers = [3, 1, 8, 7]
print(min(random_numbers))
print(max(random_numbers))
print(sum(random_numbers))

# Slice a list into the 2nd and 3rd item
toppings = ['pepperoni', 'salami', 'mushrooms', 'parmesan']
print(toppings[1:3])

# Slice into the last 3 items in the list
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[-3:])

# Loop through a list and change 'bmw' to uppercase and rest to title case
cars = ['bmw', 'audi', 'benz']
for i in cars:
	if i == 'bmw':
		print(i.upper())
	else:
		print(i.title())

# Check if a username already exists
usernames = ['xdodger27', 'elitesavage1']
user = 'xdodger26'
if user not in usernames:
	print("The username " + user + " is available")

# Using an else if
age = 21
if age < 10:
	price = 5
elif 10 < age <= 18:
	price = 10
else:
	price = 12
print("Your total cost is $" + str(price) + ".")

# Assigning a value in a Dictionary
alien_0 = {}
alien_0['speed'] = 'fast'
print("The alien's speed is: " + alien_0['speed'])
print(alien_0)

# Looping through a dictionary
user_0 = {
	'Username': 'Jfermi',
	'First Name': 'James',
	'Last Name': 'Fermi',
}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value + "\n")

# Looping through a dictionary in sorted order and displays values
# favorite_languages = {
#	 'justin': 'python',
#	 'tony': 'c',
#	 'lien': 'javascript'
# }
# for key in favorite_languages:
#	 print(key.title() + "'s favorite language is: " +
#	 favorite_languages[key])
# 	 print("\n")


# Use continue to print only the odd numbers from 1-10
currentNumber = 0
while currentNumber < 10:
	currentNumber += 1
	if currentNumber % 2 == 0:
		continue
	print(currentNumber)

# Defines a function to print Sarah's name and favorite color
def greet_user(username = 'none', favorite_color = 'none'):
	"""Greet's a user by name and their favorite color"""
	print("Hello there, " + username.title() + ", you're favorite color"
		" is " + favorite_color)
greet_user('Justin', 'blue')

# Optional parameter in a function
def get_formatted_name(first_name, last_name, middle_name = ""):
	"""Returns a formatted name where the middle name is optional"""
	if (middle_name):
		full_name = first_name + " " + middle_name + " " + last_name
	else: 
		full_name = first_name + " " + last_name
	return full_name.title()
print(get_formatted_name('Justin', 'Ng', 'River'))



