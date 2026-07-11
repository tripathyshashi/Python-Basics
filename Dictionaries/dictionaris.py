# Dictionary in Python
# key:value pairs(format)
print("Dictionary in Python")       #1
info = {
    "Name": "Shashi",
    "CGPA": 7.8,
    "Subject": ["Maths", "C", "Electronics", "Python"],
}

print(info)                 #2
print(f"\nThe type is : {type(info)}")              #3
# print(type(info))


# like we do have index value in tuples,lists same we have 'keys' here
print("Name : ", info["Name"])#4
print("CGPA : ", info["CGPA"])#5
print("Subject : ", info["Subject"])#6


# dictionaries are mutable that means we can reassign the value
info["Name"] = "Definite"
print("\nThe new value of name is assigned \nThat means dictionaries are mutable")#7
print(
    "\n\tNew Name : ", info["Name"]
)  # dictionaries are unordered that means they are not arranged in orders


# Methods associated in dictionaries
# d.keys()          return all the keys
# d.values()        return all the values
# d.items()         returns (key,val) pairs
# d.get(val)        returns val acc. to key
# d.update(new_item)    add new item to dictionaries

print("\nTo print the keys : ")  # keys are like index in lists
print(info.keys())

# we can assign it to another values
dict_vals = info.keys()
print(dict_vals)
# we can even change the type here
print("\nwe can even change the type here")
print("Now these are in lists")
dict_vals = list(info.keys())
print(dict_vals)
print(type(dict_vals))

# d.items (shows all the items stored along with there value)
print("\n", info.items())
info["CGPA"] = 9.6  # updated the value of CGPA
print(info["CGPA"])  # new CGPA
print("Here we updated cgpa value")
print(info.items())


#   d.get(val)  this is useful even we can do the same task with #d.keys but if we get any error there the program will stop but instead when
#   we use d.get(val) it will return with None when there is error in the program then executes the next line
print("\n", info.get("cgpa"))
print("this line is executed\n\n")
# print(info["cgpa"])
# print("this line won't be executed because the above line is incorrect\n\n")


#   d.update(new_item)
info.update({"city": "Delhi"})
print(info, "\n")

print(
    "All the three out of five things that we learned there results are down here and two are just up here : \n "
)
print(info.keys())
print(info.values())
print(info.items())
