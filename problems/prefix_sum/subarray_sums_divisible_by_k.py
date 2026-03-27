# 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# 
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
#
# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
# Input: nums = [5], k = 9
# Output: 0

from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        p_dict = defaultdict(int)
        p_dict[0] += 1
        count, prefix = 0, 0
        for num in nums:
            prefix += num
            remainder = prefix % k
            count += p_dict[remainder]
            p_dict[remainder] += 1
        return count
            

if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraysDivByK(nums=[4,5,0,-2,-3,1], k=5) == 7
    assert sol.subarraysDivByK(nums=[5], k=9) == 0
