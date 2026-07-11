num = [23,34,12,2,89,3,10,67,32]
print(num)
idx = 0
x=int(input("\nEnter the number from the above given numbers : "))

for val in num:
    if (val==x):
        print(f"The value of index locaation of {x} is at : {idx}")               #f-strings  #the same line can be written as below
        #f-strings are far more better we can use multiple variable in a single line very easily
        
        print("The value of index locaation is : {}".format(idx))       #format strings
        break
    idx+=1