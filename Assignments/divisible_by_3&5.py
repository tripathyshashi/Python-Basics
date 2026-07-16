# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
# Date : 15/07/2026
# Programmer : Shashi


def start(a, b):
    c = a
    found = False
    if a > b:
        print("\nInvalid Entry!!\nStarting number must be lower than ending number ")
    else:
        while a <= b:
            if a % 3 == 0 and a % 5 == 0:
                print(a)
                found = True
            a += 1

    if found == False:
        print(f"\n\tNo such value between {c} & {b}")


a = int(input("Enter the starting number : "))
b = int(input("Enter the ending number : "))
start(a, b)
