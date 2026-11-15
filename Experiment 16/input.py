
import re
from collections import Counter

# Customer reviews dataset
reviews = """
This product is very good.
The product quality is good.
I like this product very much.
The quality is excellent.
"""

# Convert text into lowercase
reviews = reviews.lower()

# Extract words
words = re.findall(r'\b\w+\b', reviews)

# Calculate word frequency
frequency = Counter(words)

# Display the result
print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
