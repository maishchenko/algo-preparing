# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# 
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# l e e t c o d e | len = 8
# 0 1 2 3 4 5 6 7
#
# t c o d e -> [3:8]

# l e e t o | len = 5
# 0 1 2 3 4

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        n = len(needle)
        for i in range(0, len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr(haystack="sadbutsad", needle="sad") == 0
    assert sol.strStr(haystack="leetcode", needle="leeto") == -1
    
    