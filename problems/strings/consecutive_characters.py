# 1446. Consecutive Characters
# https://leetcode.com/problems/consecutive-characters/description/
#
# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.
# 
# Example 1:
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

# Example 2:
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.


class Solution:
    def maxPower(self, s: str) -> int:
        current_char = s[0]
        cur_power, max_power = 0, 0
        for char in s:
            if current_char == char:
                cur_power += 1
            else:
                max_power = max(max_power, cur_power)
                current_char = char
                cur_power = 1
        max_power = max(max_power, cur_power)
        return max_power
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxPower("leetcode") == 2
    assert sol.maxPower("abbcccddddeeeeedcba") == 5