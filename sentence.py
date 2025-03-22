sentence = "The quick brown fox jumps over the lazy dog"

long_words = [word for word in sentence.split() if len(word) > 4]
print(long_words)




**Explanation:** The `split()` method breaks the sentence into words, and the condition filters out words whose length is greater than 4.

