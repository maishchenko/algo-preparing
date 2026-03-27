# 849. Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to the closest person.

# Example 1
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        max_distance = 0
        last_idx = -1
        n = len(seats)
        for i in range(n):
            if seats[i] == 1:
                if last_idx == -1:
                    max_distance = max(max_distance, i)
                else:
                    max_distance = max(max_distance, (i - last_idx) // 2)
                last_idx = i
        max_distance = max(max_distance, n - 1 - last_idx)
        return max_distance
       

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxDistToClosest(seats=[1,0,0,0,1,0,1]) == 2
