# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


# [16, 1, 0, 9, 10]
#
# l -> 16 | r -> 10 | num = [10, 1, 0, 9, 16]
# 

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square >= right_square:
                res[i] = left_square
                left += 1
            else:
                res[i] = right_square
                right -= 1
        return res
        
if __name__ == "__main__":
    sol = Solution()
    
    # example 1
    nums = [-4,-1,0,3,10]
    res = sol.sortedSquares(nums)
    assert res == [0, 1, 9, 16, 100]
    
    # example 2
    nums = [-7,-3,2,3,11]
    res = sol.sortedSquares(nums)
    assert res == [4,9,9,49,121]
