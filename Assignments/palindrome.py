# Ask the user for a string and check whether it is a palindrome or not.

pal = input("Enter the elements : ")
pal = pal.upper()
print(f"\nThe entered string is : {pal}\n")

if "".join(reversed(pal)) == pal:
    print("\tPalindrome")
else:
    print("\tNon Palindrome")
