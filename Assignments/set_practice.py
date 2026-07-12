# Given a list of tuples with info(name, subject):
# 1. list all unique course
# 2. list students enrolled in English
# 3. create dictionary (student, set of courses)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

print("1. The information listed above : ")
print(info, "\n")
courses_set = set()

for tup in info:
    courses_set.add(tup[1])
print("\nThe unique courses are : ", courses_set)


# we can print like this aswell
# for name , course in info:
#     print(name,course)
print("\n2. The students enrolled in English are : ")
for tup in info:
    if tup[1] == "English":
        print("\t", tup[0])


dict = {}
print("\n3. The selected courses of each student are : ")
for tup in info:
    if dict.get(tup[0]) == None:
        dict.update({tup[0]: set()})
        dict[tup[0]].add(tup[1])
    else:
        dict[tup[0]].add(tup[1])

print(dict)