# Program to print the reverse of entered number.
# Date : 15/07/2026
# Programmer : Shashi

print("Program to print the reverse of entered number.")


def sum_digit(n):
    sum = 0
    divisor = 10
    while n > 0:
        a = n % divisor
        # print(a)  #this prints all the entered digit in reverse
        sum += a
        n = n // divisor
    print(f"\nThe sum of entered digits is {sum}")


n = int(input("Enter the number : "))
sum_digit(n)
