word = "Python"

# to print by the address of strings_______e.g
print(word[0], word[1], word[2], word[3], word[4], word[5],"\n")

#we can also use 'for' loop instead of typing multiple times
#as the string is character value...will 'ch' variable
#string in python is immutable that means once we assign a value... it can't be assigned twice in the excisting string

for ch in word:
    print(ch)
    
    
print(len(word),"\n")


# concatenate = adding of two strings_______e.g
word1 = "I Love"

print(word1 + " " + word)

#we can even print one o two characters from the middle of a strings

print(word[2:4])
#when we want to print until the end of a string from the middle of somewhere,
#we leave the space blank of ending syntex here '4' in the above string______e.g

wd="Welcome to my ERA ..this is my programming world"
print(wd[20:])          #here we left the ending space empty so it prints till the end of the string

#by default the starting value is 0 and the ending value is len(w) that is length of the string 


#even we can take it in negative assigned_______-e.g

print(word[-4:-2]) #both statements print the same value that is th