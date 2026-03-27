# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        prefix, total_counts = 0, 0
        for num in nums:
            prefix += num
            total_counts += prefix_sum[prefix - k]
            prefix_sum[prefix] += 1
        return total_counts


if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraySum(nums=[1,1,1], k=2) == 2
    assert sol.subarraySum(nums=[1,2,3], k=3) == 2
