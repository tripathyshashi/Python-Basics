# Write a function to return the count the number of digits in a number, n.
# Date : 15/07/2026
# Programmer : Shashi

print("Program to return the count of number of digits in a number, n.")


def count_digit(n):
    divisor = 10
    count = 0
    while n > 0:
        a = n % divisor
        n = n // 10
        count += 1

    print(f"The count of entered number is : {count}")


n = int(input("Enter the number : "))
count_digit(n)
