age = int(input("Enter the age : "))

if (age < 13):
    print("\tChild")
elif (age>=13 and age<19):
    print("\tTeenager")
elif (age>=19 and age<60):
    print("\tAdult")
else:
    print("\tSenior Citizen")