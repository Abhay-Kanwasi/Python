# string replacement practice

weight = 20
print("My weight is " + str(weight) + "kg")  # concating int in a string

# cleaner approach to print weight
print("My weight is {0} kgs".format(weight))

# printing multiple values
print("hello {0},{1},{2}".format("ron", "harry", "harmonie"))

# changing index changes order of values
print("hello {1},{2},{0}".format("ron", "harry", "harmonie"))


# formating strings

for i in range(1, 11):
    # second arg provide padding\extra space of given number in variable
    print("number {0:3} , square {1:4} , cube {2:4}".format(i, i**2, i**3))

    # < sign left align && ^ symbol middle align the output while formatting
    print("number {0:3} , square {1:<4} , cube {2:^4}".format(i, i**2, i**3))
