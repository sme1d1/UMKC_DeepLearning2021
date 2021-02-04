# sme1d1 Scott McElfresh 1/22/2021
import random

# assign user input to name
name = input("Enter a word: ".lower())

# assign string characters to a list so they can be modified
name_list = list(name)

# pick some random number between 0 and the length of the word
# -1 so we can use the value as an index
x = random.randint(0, len(name)-1)
y = random.randint(0, len(name)-1)
# ensure that we don't pick the same random value
while x == y:
    y = random.randint(0, len(name)-1)
print("Removing #%d character: %s" % (x+1, name_list[x]))
print("Removing #%d character: %s" % (y+1, name_list[y]))

#replace list characters
name_list[x] = ''
name_list[y] = ''

#assign list characters to new string
new_name = "".join(name_list)

# print the new reversed word
print("Reversed word with missing characters: ")
print(new_name[::-1])

a = int(input("\nEnter an integer: "))
b = int(input("Enter a second integer: "))
c = a + b
d = a * b
e = a/b
print("The sum of %d and %d, is %d" % (a, b, c))
print("%d multiplied by %d, is equal to %d" % (a, b, d))
print("%d divided by %d, is equal to %f" % (a, b, e))
