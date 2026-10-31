
# Create a text file
file = open("sample_text.txt", "w")
file.write("Python is easy. Python is powerful. Python is interesting.")
file.close()

# Open the file in read mode
file = open("sample_text.txt", "r")

text = file.read()
file.close()

# Convert text into lowercase words
words = text.lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?")

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency Distribution:")

for word, count in frequency.items():
    print(word, ":", count)
