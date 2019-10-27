# This function creates a dictionary for each word and counts the number of times
# a letter occurs in it as a value and the letter as the key and prints the dictionary for the word

def most_frequent(s):
    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    print(t)
    return res

def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist
        
# A header line is printed with the language type that will be analyzed
print ('*'*120)
print ('English')
print ('*'*120)

# A counter for the number of words analyzed in the file is set to zero
count = 0

# The file is opened first and the line is imported
# In the for loop the words are split out and passed into the most_frequent function
# A statement is then printed about the word number and the histogram for the word sorted descending

with open('english.txt','r') as f:
    for line in f:
        for word in line.split():
            print('Most frequent letters in', word, 'are')
            h = most_frequent(word)
            count = count + 1

# After all words have been analyzed the total number of words is printed

print(count)

# A header line is printed with the language type that will be analyzed
print ('*'*120)
print ('French')
print ('*'*120)

# A counter for the number of words analyzed in the file is set to zero
count = 0

# The file is opened first and the line is imported
# In the for loop the words are split out and passed into the most_frequent function
# A statement is then printed about the word number and the histogram for the word sorted descending

with open('french.txt','r') as f:
    for line in f:
        for word in line.split():
            print('Most frequent letters in', word, 'are')
            h = most_frequent(word)
            count = count + 1

# After all words have been analyzed the total number of words is printed

print(count)

# A header line is printed with the language type that will be analyzed
print ('*'*120)
print ('German')
print ('*'*120)

# A counter for the number of words analyzed in the file is set to zero
count = 0

# The file is opened first and the line is imported
# In the for loop the words are split out and passed into the most_frequent function
# A statement is then printed about the word number and the histogram for the word sorted descending

with open('german.txt','r') as f:
    for line in f:
        for word in line.split():
            print('Most frequent letters in', word, 'are')
            h = most_frequent(word)
            count = count + 1

# After all words have been analyzed the total number of words is printed

print(count)
