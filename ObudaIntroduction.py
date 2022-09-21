import sys
#Introductions,
#PyCharm,
#variables,
#operators, print,
#input
# Use standard input to enter your full name into a variable. The name of the variable should be var1.
var1 = input('Enter your full name:')
# Store the fourth character (index) of var1 in the variable var2.
var2 = var1[4]
print(var2)
# Assigns the character's ASCII code (var2) to the variable var3.
var3 = ord(var2)
print(var3)
# Use the var3 variable to calculate the following:
# - Add 11 (decimal).
print(var3+11)

# - Subtract 11 (hexadecimal).
print(hex(var3-11))
# - Multiply by 21 (octal).
print(oct(var3*21))
# - Divide by 1011 (binary).
print(bin(var3))
print(var3/1011)
# - Divides var3 by 9 (decimal) and returns the remainder.
print(var3/9)
# Print the result of each operation to standard output.

# The program closes with the following error stream: End of code!
sys.stderr.write('End of code')
