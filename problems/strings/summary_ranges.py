# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/description/
#
# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start, end = 0, 1
        intervals = []
        while end < len(nums):
            if nums[end] - nums[end-1] != 1:
                # записываем интервал
                start_num = nums[start]
                end_num = nums[end-1]
                if start_num == end_num:
                    intervals.append(str(start_num))
                else:
                    intervals.append(f"{start_num}->{end_num}")
                start = end
            end += 1

        start_num = nums[start]
        end_num = nums[end-1]
        if start_num == end_num:
            intervals.append(str(start_num))
        else:
            intervals.append(f"{start_num}->{end_num}")
        
        return intervals
    

if __name__ == "__main__":
    sol = Solution()
    assert sol.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert sol.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
