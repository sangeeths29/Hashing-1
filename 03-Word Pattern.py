# Problem 3 - Word Pattern (https://leetcode.com/problems/word-pattern/)
# Check if each character in the pattern can be uniquely mapped to a word in the string
# Mapping must be consistent and bijective
# If all pairs satisfy this condition, return True else False
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}   # maps each pattern character -> word
        used_words = set()  # keeps track of words already assigned to some pattern character
        
        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                char_to_word[char] = word
                used_words.add(word)
        
        return True