file = open("sample_text.txt", "r")

text = file.read()

file.close()

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
