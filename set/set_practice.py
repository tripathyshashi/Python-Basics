info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

print(info, "\n")
courses_set = set()

for tup in info:
    print(tup[0], "\t", tup[1])
    # print (tup [1]) #course

for tup in info:
    courses_set.add(tup[1])

print(courses_set)
