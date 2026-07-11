def digit():
    n = int(input("Enter the digit : "))        #input
    count = 0
    while n>0:
        d = n%10
        n = n//10
        count += 1
        print(d)
    print("The count of digits : ",count)   
digit()