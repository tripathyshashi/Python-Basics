# Program to print the reverse of entered digit
# Date : 15/07/2026
# Programmer : Shashi

print("Program to print the reverse of entered number.")


def print_int(n):
    divisor = 10
    while n > 0:
        a = n % divisor
        print(a)
        n = n // divisor


n = int(input("Enter the number : "))
print_int(n)
