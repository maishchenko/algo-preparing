# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
#
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_counter = Counter(p)
        
        start, end = 0, len(p)
        s_counter = Counter(s[start:end])
        start_anagram_indexes = []
        if p_counter == s_counter:
            start_anagram_indexes.append(start)

        for end in range(len(p), len(s)):
            s_counter[s[end]] += 1
            s_counter[s[start]] -= 1
            if s_counter[s[start]] == 0:
                del s_counter[s[start]]
            start += 1
            if s_counter == p_counter:
                start_anagram_indexes.append(start)
                
        return start_anagram_indexes
        
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.findAnagrams(s="cbaebabacd", p="abc") == [0,6]
    assert sol.findAnagrams(s="abab", p="ab") == [0, 1, 2]
    