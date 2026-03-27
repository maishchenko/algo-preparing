# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/
#
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1
# Input: s = "abc", t = "ahbgdc"
# Output: true 
#
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# a : pointer = 1
# b : pointer = 2
# c : pointer = 3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True
        pointer = 0
        for char_t in t:
            if char_t == s[pointer]:
                pointer += 1
                if pointer == len(s):
                    break
        if pointer != len(s):
            return False
        return True
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.isSubsequence(s="abc", t="ahbgdc")
    assert not sol.isSubsequence(s="axc", t="ahbgdc")
