# precision anf fstring in python

# printing a simple calculation

print("{0}".format(22/7))  # default precision in python is till 15th place

# set vales t00 5 floating point values
print("{0:.5f}".format(22/7))


# using fstring
# f character before string declears that string includes some variable
# this concept is somwhat similar to jsx where ` ` are used to declear variables in string
print(f"My bmi is : {60/1.7:.2f} ")

# string interpolation (for python 2 only)

weight = 42
name = "abhay"
print("my name is : %s and my weight is %d" % (name, weight))
