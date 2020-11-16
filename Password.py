import random
import clipboard

gotString = False
order = []
password = ""
noCap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
capitalized = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "?", "'", ">", ",", ".", "<"]
choices = [noCap, capitalized, numbers, symbols]

try:
    length = int(input("How long should the password be? (Default length is 16 characters) "))
except Exception:
    length = 16

for i in range(0, length):
    order.append(random.choice(choices))
    password += random.choice(order[i])

clipboard.copy(password)
print("The password {} has been copied to clipboard.".format(password))

input("Press any key to exit.")