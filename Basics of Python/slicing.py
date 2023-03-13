str = "abcdefghijklmnopqrstuvwxyz"

print(str[0:5])  # does not include 5th index char
print(str[2:5])  # includes 2nd index char but does not include 5th index char

print(str[:5])  # not including first argument will print from start
print(str[3:])  # not including second argument will print till end

print(str[-5:-2])  # slice from back of string


#  step slicing in strings

# third arg while slicing represent steps taken while printing strings
print(str[0:24:3])

# backward slicing in python

# adding third arg as -1 which is step argument takes reverse steps
print(str[24:0:-1])
