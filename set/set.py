# set
#   set are mutable and unordered, it won't print the same element multiple time even if we enter the same element multiple times,
#   and it takes the space of only those elements that it prints


s = {1, 2, 3, 4, 3, 2, 4}
print(s)
print(type(s))
print(len(s))

# s.add(val)      #adds a val
# we can add any value using the above syntax
print("\nwe can add any value using the above syntax s.add(x)")
s.add(5)
print(s)

# • s.remove(val)     #removes a val
# we can remove any value using the above syntax
print("\nwe can remove any value using the above syntax s.remove(y) ")
s.remove(1)
print(s)


# • s.pop()       #removes a random val
print("\ns.pop()    removes a random val")
print(s)
s.pop()
print(s)


# • s.clear()     #empties the set
print("\nwe can clear the whole set using s.clear()")
s.clear()
print(s)

# • s.union(set2)     #returns new union
# • s.intersection(set2)      #returns new intersection

s1 = {1, 2, 3, 4, 5, 1}
s2 = {9, 7, 2, 6, 1}
print("\ntwo new sets are", "\nset 1 : ", s1, "\nset 2 : ", s2)
print("\nunion")
print(s1.union(s2))
print("\nintersection")
print(s1.intersection(s2))