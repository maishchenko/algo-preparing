# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
# 
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# 
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

from collections import defaultdict

# e i d b a o o o
# 0 1 2 3 4 5 6 7
#
# len(s2) = 8
# s2[6:8] -> s2[6:len(s2)] -> o o (последние два символа)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        chars_s1 = defaultdict(int)
        for c in s1:
            chars_s1[c] += 1
        
        chars_sub_s2 = defaultdict(int)
        start, end = 0, len(s1)
        for c in s2[start:end]:
            chars_sub_s2[c] += 1
            
        if chars_s1 == chars_sub_s2:
            return True
            
        for end in range(len(s1), len(s2)): # range(2, 8) -> [2, 3, ..., 8]
            chars_sub_s2[s2[end]] += 1
            
            chars_sub_s2[s2[start]] -= 1
            
            if chars_sub_s2[s2[start]] == 0:
                del chars_sub_s2[s2[start]]
                
            if chars_s1 == chars_sub_s2:
                return True
            start += 1
        
        return False
    

if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion(s1="ab", s2="eidbaooo")
    assert not sol.checkInclusion(s1="ab", s2="eidboaoo")
    