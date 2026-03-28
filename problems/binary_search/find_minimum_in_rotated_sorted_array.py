# 153. Find Minimum in Rotated Sorted Array

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 


# Надо найти максимальный элемент 
#
# 2 эдж кейса:
# 1 Максимальный элемент по индексу len(num) - 1 
#       -> значит список отсортирован правильно и минимальный эл-т по индексу 0
# 2 Любое другой индекс -> значит мин эл-т по индексу максимального плюс 1
# 

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            return nums[0]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid 
            else:
                left = mid + 1
        return nums[left]
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([4,5,6,7,0,1,2]) == 0
    