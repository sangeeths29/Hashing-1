# Problem 2 - Isomorphic Strings (https://leetcode.com/problems/isomorphic-strings/)
# Check for 1-1 mapping from characters in s to characters in t by storing s->t pairs in a map and simultaneously ensuring no two different s-characters map to same t-character using a seen set for t
# If a previosuly mapped character conflicts or a new mapping tries to reuse a t-character already taken, we return False; otherwise True
# Runs in O(n) time and O(m) space where m is the character set size
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Approach 1
        # if len(s) != len(t):
        #     return False
        # sMap = {}
        # tMap = {}

        # for i in range(len(s)):
        #     sChar = s[i]
        #     tChar = t[i]
        #     if sChar in sMap:
        #         if sMap[sChar] != tChar:
        #             return False
        #     else:
        #         sMap[sChar] = tChar
            
        #     if tChar in tMap:
        #         if tMap[tChar] != sChar:
        #             return False
        #     else:
        #         tMap[tChar] = sChar
        # return True

        # Approach 2
        # if len(s) != len(t):
        #     return False
        
        # sMap = [None] * 256
        # tMap = [None] * 256

        # for i in range(len(s)):
        #     sChar = s[i]
        #     tChar = t[i]
        #     indexS = ord(sChar)
        #     indexT = ord(tChar)

        #     if sMap[indexS] != None:
        #         if sMap[indexS] != tChar:
        #             return False
        #     else:
        #         sMap[indexS] = tChar
            
        #     if tMap[indexT] != None:
        #         if tMap[indexT] != sChar:
        #             return False
        #     else:
        #         tMap[indexT] = sChar
        # return True

        # Approach 3
        if len(s) != len(t):
            return False
        sMap = {}
        tSet = set()
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sMap:
                if sMap[sChar] != tChar:
                    return False
            else:
                if tChar in tSet:
                    return False
            
            sMap[sChar] = tChar
            tSet.add(tChar)
        return True
