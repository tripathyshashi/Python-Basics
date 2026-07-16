#formatting strings.    can be done by format() & f-strings....the example is shown below
#the given examples are defined by using 'format()'  strings


a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
sum=a+b
print("The sum of {} and {} is {}".format(a,b,sum))


print("Index based formatting")
print("The sum of {1} and {0} is {2}".format(a,b,sum))


print("Value based formatting")
#we can even use it for specify direct variables
print("\nThis is {} and this {} {}".format("Python","is my favourite one","and i hope it'll help me get well far to tech career"))


print("Value based formatting")
#we can even use it for specify direct variables
print("The value is {c} and {d}".format(c=5,d=7))