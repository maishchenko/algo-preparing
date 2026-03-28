# 2367. Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/description/
#
# Example 1:
# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set: set[int] = set(nums)
        count = 0
        for num in nums:
            if num + diff in nums_set and num + 2 * diff in nums_set:
                count += 1
        return count
    
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.arithmeticTriplets([0,1,4,6,7,10])
