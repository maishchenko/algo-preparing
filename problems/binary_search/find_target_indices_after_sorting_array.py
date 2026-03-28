# 2089. Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        idx = self.binary_search(nums, target)
        if idx == -1:
            return []
        
        left, right = idx, idx
        indexies = set()
        while left >= 0 and nums[left] == target:
            indexies.add(left)
            left -= 1
        
        while right < len(nums) and nums[right] == target:
            indexies.add(right)
            right += 1

        indexies = sorted(list(indexies))
        return indexies

    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

        
if __name__ == "__main__":
    sol = Solution()
    assert sol.targetIndices(nums=[1,2,5,2,3], target=2) == [1, 2]
    