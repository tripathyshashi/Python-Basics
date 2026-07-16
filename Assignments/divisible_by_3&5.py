# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
# Date : 15/07/2026
# Programmer : Shashi


def start(a):
    while a <= b:
        if a % 3 == 0 and a % 5 == 0:
            print(a)
        a += 1


a = int(input("Enter the starting number : "))
b = int(input("Enter the ending number : "))
start(a)
