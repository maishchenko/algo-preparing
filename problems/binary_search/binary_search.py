nums = [1, 2, 4, 6, 8, 12, 18]
target = 8 # idx = 4

def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else: # nums[mid] > target
            right = mid - 1
    return -1

# print(binary_search(nums=[1, 2, 4, 6, 8, 12, 18], target=8))  # 4
# print(binary_search(nums=[1, 2, 4, 6, 8, 12, 18], target=1))  # 0
# print(binary_search(nums=[1, 2, 4, 6, 8, 12, 18], target=18)) # 6
# print(binary_search(nums=[1, 2, 4, 6, 8, 12, 18], target=19)) # -1
# print(binary_search(nums=[1, 2, 4, 6, 8, 12, 18], target=5))  # -1


print(binary_search(nums=[0, 2, 2, 8, 12, 18], target=2))
#                         0  1  2  3  4  5  6  7   8
 