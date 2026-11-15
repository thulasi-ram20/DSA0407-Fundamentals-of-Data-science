
import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

# Load CSV file
data = pd.read_csv("data.csv")

# Stop words
stop_words = {
    "the", "and", "is", "in", "to", "of",
    "a", "an", "for", "it", "this", "was",
    "are", "with", "on", "very", "i"
}

# Combine feedback
text = " ".join(data["feedback"].dropna().astype(str))

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r'[^a-z\s]', '', text)

# Split into words and remove stop words
words = [
    word for word in text.split()
    if word not in stop_words
]

# Calculate word frequency
frequency = Counter(words)

# Get N from user
n = int(input("Enter the number of top words: "))

# Display top N words
top_words = frequency.most_common(n)

print("\nTop", n, "Most Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Plot bar graph
if top_words:
    words_list, counts = zip(*top_words)

    plt.bar(words_list, counts)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top N Most Frequent Words")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No words available for plotting.")
