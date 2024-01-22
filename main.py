#Password Generator Project
import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# numChar = int(input(f"How many characters long would you like your password to be?\n"))
numLetter = int(input("How many letters would you like in your password?\n")) 
numSymbol = int(input("How many symbols would you like?\n"))
numNumber = int(input("How many numbers would you like?\n"))
ezPass = str("")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for _i in range(numLetter):
	ezPass += random.choice(letters)
for _i in range(numSymbol):
	ezPass += random.choice(symbols)
for _i in range(numNumber):
	ezPass += random.choice(numbers)

print(f"Easy mode Password: {ezPass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

ezPassList = list(ezPass)
hardPass = str("")

random.shuffle(ezPassList)
hardPass = "".join(ezPassList)

print(f"Hard Mode Password: {hardPass}")

#Structured Hard Level - Mimic MasterPassword format:
#e.g. 14 characters = BirlGult5%Solp


sys.exit()