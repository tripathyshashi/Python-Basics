def print_int(n):
    divisor = 1
    while n // divisor >= 10:
        divisor = divisor * 10
    while divisor > 0:
        a = n // divisor
        print(a)
        n = n % divisor
        divisor = divisor // 10


n = int(input("Enter the number : "))
print_int(n)
