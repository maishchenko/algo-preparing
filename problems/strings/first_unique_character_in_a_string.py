# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
# Input: s = "aabb"
# Output: -1

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_chars = defaultdict(int)
        for char in s:
            s_chars[char] += 1
        for idx, char in enumerate(s):
            if s_chars[char] == 1:
                return idx
        return -1 
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.firstUniqChar(s="leetcode") == 0
    assert sol.firstUniqChar(s="loveleetcode") == 2
    assert sol.firstUniqChar(s="aabb") == -1
