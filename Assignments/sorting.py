list1 = list(map(int, input("Enter the elements : ").split()))
print(f"List 1 : {list1}")
list2 = list(map(int, input("\nEnter the elements : ").split()))
print(f"List 2 : {list2}")

res = list1 + list2
res.sort()
print(f"The sorted result is : {res}")