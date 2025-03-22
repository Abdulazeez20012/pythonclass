words = ["madam", "racecar", "hello", "level", "world"]




palindromes = [word for word in words if word == word[::-1]]
print(palindromes) 

**Explanation:** The slicing `[::-1]` reverses each word, and the condition checks if a word is the same as its reversed version.

---
