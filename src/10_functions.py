# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x % 2 == 0:
        return True

# print(is_even(2))
# print(is_even(1))

# Read a number from the keyboard
# num = input("Enter a number: 3")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even_or_odd(num):
    if num % 2 == 0:
        return "Even!"
    else: 
        return "odd"

print(even_or_odd(2))
print(even_or_odd(1))