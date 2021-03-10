
#wordcount
happy = input()

print("Enter any statement: ")
words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
