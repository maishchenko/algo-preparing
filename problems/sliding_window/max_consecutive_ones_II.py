# 487. Max Consecutive Ones II (subscribe)
# https://leetcode.com/problems/max-consecutive-ones-ii/
#
# Дан бинарный массив nums из нулей и единиц. Найди максимальное количество consecutive единиц, 
# если разрешено перевернуть не более одного нуля в единицу.
#
# Пример:
# nums = [1, 0, 1, 1, 0]
# Если перевернуть первый 0 → [1, 1, 1, 1, 0] — получаем 4 единицы подряд.
# Если перевернуть последний 0 → [1, 0, 1, 1, 1] — получаем 3 единицы подряд.

class Solution():
    def maxConsecutiveOnes(self, nums: list[int]) -> int:
        if not nums:
            return 0
        zero_count = 0
        start, end = 0, 0
        max_length = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxConsecutiveOnes([1, 0, 1, 1, 0]) == 4
    assert sol.maxConsecutiveOnes([]) == 0
    assert sol.maxConsecutiveOnes([0]) == 1
    assert sol.maxConsecutiveOnes([0, 1]) == 2
    assert sol.maxConsecutiveOnes([0, 1, 0, 0, 0]) == 2
    assert sol.maxConsecutiveOnes([1, 1, 1, 1, 1]) == 5
