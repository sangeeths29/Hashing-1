# Problem 1 - Group Anagrams (https://leetcode.com/problems/group-anagrams/)
# Map each word to a key which uniquely represents its letter multiset by multiplying primes assigned to letters; anagrams produce identical products
# Use a hash map from this prime-product key to the list of words; append each word to its bucket in O(1) expected time
# Overall time is O(N*k) where N is number of words and K is average word length; Python's big integers avoid overflow for prime products
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            primeProduct = self.primeProduct(s)
            if primeProduct not in map:
                map[primeProduct] = []
            map[primeProduct].append(s)
        
        return list(map.values())
    
    def primeProduct(self, s : str) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
        result = 1
        for i in range(len(s)):
            c = s[i]
            result = result * primes[ord(c) - ord('a')]
        return result