# In Python, a loop is used to iterate (loop) over a sequence, such as a list, tuple,
# string, or range, and execute a block of code for each item in that sequence.

#range(n) means sequence from 0 to (n-1) 
#for i in range(5):
   # print(i+1)
    
count=0
word=input("Enter a word : ")   #counting 'i' in provided word
for ch in word:
    if(ch=='i'):
        count+=1
        
print("\nThe count of i in the given word  is",count)

vowel=0
for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        vowel+=1
print("\nThe count of vowel letters is ",vowel)