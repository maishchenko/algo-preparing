# 356. Line Reflection (subscribe)
# https://leetcode.com/problems/line-reflection/description/
#
# Даны n точек на плоскости. Нужно определить существует ли вертикальная линия такая что при отражении всех точек относительно неё получается то же самое множество точек.
# Отражение точки (x, y) относительно вертикальной линии x = c:
# (x, y) → (2c - x, y)
# Y-координата не меняется, X-координата зеркалится.

# Примеры:
# [(1,1), (3,1)] → линия x = 2 → точка (1,1) отражается в (3,1) и наоборот → True
# [(1,1), (2,2)] → никакая вертикальная линия не даст то же множество → False


from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        s = min_x + max_x
        point_set: set[tuple[int]] = set((point[0], point[1]) for point in points)
        for point in points:
            x = point[0]
            y = point[1]
            if (s - x, y) not in point_set:
                return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.isReflected([(1,1), (3,1)])
