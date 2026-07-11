# Programmer : Shashi
# Date    :   07/07/2026
#


# #Tuples           sequence of values
# Tuples are immutable that means we can't change the assigned value more than once
# Tuples are similar as Lists
# The only difference is that lists are mutable but Tuples are not

tup = (1, 2, 3.14, 4, 8, 5, 6, 9, 11, 7)
print("The entered elements in tuples are")
print(tup)
print(tup[2])
print(type(tup))
print(len(tup))

# in tuple when we execute only one value in the tuple it print that value what it is
# e.g here it print it as an integer
print("\nprinting types")
tuple = 1
print(type(tuple))

# e.g here it print it as an string
mine = "abc"
print(type(mine))

# now it'll print it as a tuple because we used comma after the single value
st = (1,)
print(type(st))

# for lists
# here it'll print it as a list even if it has a single digit inside it.       this is one of the difference between lists and tuple
list = [2]
print(type(list))

# we can even do slicing as we did in lists with the same method
print("\nSlicing methods")
print(tup[2:5])  # it'll print till the range entered inside    tup[2:5:1] where 2 is staring index_5 is ending index and 1 is executing index
print(tup[:5])  # it'll print from the starting
print(tup[2:])  # it'll print it till the end

# Loops
# as we used loops in lists same we can use loops here in Tuples
print("\nused loops here")
sum = 0
for val in tup:
    sum += val
print(f"The sum of these {tup} listd numbers is : {sum}")


#we can even print the index value directly in Tuples
print("\nwe can even print the index value directly in Tuples")
print(tup.index(4))

#we can even count the same element in a list 
print("\nwe can even count the same element in a list ")
m = (2,1,45,3,2,2,5,4,9,2)
print(f"The given list is {m}")
y=int(input("\nEnter the number that has to be find in the above list : "))
print(f"The count of {y} is ")
print(m.count(y))           #count function (t.count(x))         where 'x' is one of the elements from the list