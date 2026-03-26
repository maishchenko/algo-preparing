# 159. Longest Substring with At Most Two Distinct Characters (subscribe)
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/ 

# Дана строка s. Найди длину наидлиннейшей подстроки, которая содержит не более двух различных символов.

# Примеры:
# s = "eceba" → 3, подстрока "ece" (символы 'e' и 'c')
# s = "ccaabbb" → 5, подстрока "aabbb" (символы 'a' и 'b')

import collections

class Solution():
    def findLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        chars_dict = collections.defaultdict(int)
        start, end = 0, 0
        max_length = 0
        for end in range(len(s)):
            chars_dict[s[end]] += 1
            while len(chars_dict) > 2:
                chars_dict[s[start]] -= 1
                if chars_dict[s[start]] == 0:
                    del chars_dict[s[start]]
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

if __name__ == "__main__":
    sol = Solution()
    assert sol.findLongestSubstring("eceba") == 3
    assert sol.findLongestSubstring("ccaabbb") == 5
    assert sol.findLongestSubstring("") == 0
    assert sol.findLongestSubstring("a") == 1
    assert sol.findLongestSubstring("aab") == 3
