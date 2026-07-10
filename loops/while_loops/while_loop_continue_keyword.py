#odd or even using continue keyword

print("Program to print Odd or Even")
n = int(input("Enter the limit : "))
i=0
while(i<n):
    i+=1
    #if((i+1)%2==0): #for even
    if(i%2==0): #for odd
        continue
    print(i)