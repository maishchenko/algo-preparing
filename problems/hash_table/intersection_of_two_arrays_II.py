# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        intersection = []
        for n in nums2:
            if counter[n]:
                intersection.append(n)
                counter[n] -= 1
        return intersection
    

if __name__ == "__main__":
    sol = Solution()
    assert sol.intersect(nums1=[1,2,2,1], nums2=[2,2]) == [2, 2]