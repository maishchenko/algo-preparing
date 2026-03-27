# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point_to_write = len(nums1)-1
        
        while m > 0 and n > 0 and point_to_write >= 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[point_to_write] = nums1[m-1]
                m -= 1
            else:
                nums1[point_to_write] = nums2[n-1]
                n -= 1
            point_to_write -= 1
            
        while m > 0 and point_to_write >= 0:
            nums1[point_to_write] = nums1[m-1]
            m -= 1
            point_to_write -= 1
            
        while n > 0 and point_to_write >= 0:
           nums1[point_to_write] = nums2[n-1]
           n -= 1
           point_to_write -= 1
           
        
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1,2,2,3,5,6]
    