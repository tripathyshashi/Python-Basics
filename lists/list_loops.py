#loop in lists

print("the list is")
num=[4,3,18,34,2]
print(num)

print("\nthe sorted list is")
num.sort()
for val in num:
    print(val)
    
print("\nsorting in reverse")
num.sort(reverse=True)
print(num)

print(num[2])