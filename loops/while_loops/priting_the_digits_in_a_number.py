# Write a function that prints the digits of a number 'n'
# n = 312
# For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them.
# Date : 15/07/2026
# Programmer : Shashi

n = int(input("Enter the number : "))

divisor = 1
while n // divisor >= 10:
    divisor = divisor * 10
while divisor > 0:
    a = n // divisor
    print(a)
    n = n % divisor
    divisor = divisor // 10
