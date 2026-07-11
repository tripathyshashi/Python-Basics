#Lists #tuples #Dictionaries #Sets
#Firstly we'll discuss list here 
#Lists is the mutable sequence of values


marks = [12,34,56,33,445,23]
marks[4]=43                 #Lists are mutable that means we can assign a value again and again that wasn't possible in strings
print(marks)
marks[4]=23
print(len(marks))
print(marks[0],"\t",marks[1],marks[2],marks[3],marks[4])
print(marks[5])
print(type(marks))


#we can even perform slicing in lists as we did in strings