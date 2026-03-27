# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/
#
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
#
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        return sum(1 for char in stones if char in j)
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3
    assert sol.numJewelsInStones(jewels="z", stones="ZZ") == 0
    