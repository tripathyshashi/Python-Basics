# Create an empty dictionary
words = {}

n = int(input("Enter the number of words: "))

for i in range(n):
    word = input("Enter a word: ")
    words[word] = len(word)

print("\nDictionary:")
print(words)