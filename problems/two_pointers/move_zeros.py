# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/
#
# Given an integer array nums, move all 0's to the end of
# it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for num in nums:
            if num != 0:
                nums[pointer] = num
                pointer += 1
        for p in range(pointer, len(nums)):
            nums[p] = 0        
        
if __name__ == "__main__":
    sol = Solution()
    
    # example 1
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    assert nums == [1,3,12,0,0]
    
    # example 2
    nums = [0]
    sol.moveZeroes(nums)
    assert nums == [0]
