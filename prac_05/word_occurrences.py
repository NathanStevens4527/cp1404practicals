"""
Program for counting the number of occurrences of a word in a string
words are stored in dictionary with the number of occurrences.
"""

word_to_occurrences = {}
text = input("Text: ")
text = text.split()

for word in text:
    if word in word_to_occurrences:
        word_to_occurrences[word] += 1
    else:
        word_to_occurrences[word] = 1
sorted_word_to_occurrences = sorted(word_to_occurrences)
for word in sorted_word_to_occurrences:
    print(f"{word} : {word_to_occurrences[word]}")