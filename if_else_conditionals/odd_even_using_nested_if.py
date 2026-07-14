n = int(input("Enter the number : "))
if n > 0:
    if n % 2 == 0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")
else:
    print(f"{n} is zero.")
