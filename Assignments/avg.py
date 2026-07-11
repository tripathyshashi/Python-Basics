a = list(map(int, input(f"Enter the elements : ").split()))
print(f"The elements are : {a}")

sum=0
n=0
for val in a:
    sum+=val
    n+=1
print(f"\nThe sum of entered integer is : {sum}")
avg=sum/n
print(f"\nThe average of entered integer is : {avg}")