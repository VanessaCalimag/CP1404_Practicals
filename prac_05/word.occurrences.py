"""This program will count the occurrences of words in a string."""

text = {}
string_of_words = input('Text: ')
# This is a collection of words of nice words this is a fun thing it is

# Splitting words from user's input
words = string_of_words.split()
for word in words:
    occurrence = text.get(word, 0)
    text[word] = occurrence + 1

words = list(text.keys())
words.sort()
word_length = max((len(word)for word in words))
for word in words:
    print('{:{}} =  {}'.format(word, word_length, text[word]))
