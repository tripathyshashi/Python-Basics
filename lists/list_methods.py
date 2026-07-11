#Lists> Methods(Function)
#l.append(val)
#l.insert(idx, val)
#I.sort()
#I.reverse()

# use of Append function
print("the entered list is")
num = [18,2,33,1]
print(num)
print("\nappend a new number ")
num.append(10)
print(num)

print("\nre assigned the value of append function")
num[4]=5        #re assigned the value of append function
print(num)

print("\ninserting a value in middle of a string")
num.insert(2,2.5)   #inserting a value inside a string
#num[3]=23
print("\t",num)
print("\nwe can reverse the whole list aswell")
num.reverse()
print(num)

print("\nwe can sort the list aswell in increasing order")
num.sort()
print(num)

#we can even reverse it 
print("\nfor reverse sorting ")
num.sort(reverse=True)
print(num)