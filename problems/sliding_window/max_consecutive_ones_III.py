# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# 
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        if not nums:
            return 0
        start, end, max_length = 0, 0, 0
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
