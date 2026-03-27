# Prefix sum
#
# prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

# nums = [5, 3, 8, 1, 4, 6]
nums = [0, 1, 0, 2, 3, 0, 0, 5, 1] # len(9)
# idx   0  1  2  3  4  5  6  7  8

prefix_sum = [0] * (len(nums) + 1)
for i in range(1, (len(nums) + 1)):
    prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
#           nums    [0, 1, 0, 2, 3, 0, 0, 5,  1]
print(prefix_sum) # [0, 0, 1, 1, 3, 6, 6, 6, 11, 12]
                  #  0  1  2  3  4  5  6  7  8   9

# количество нулей на интервале от 1 до 5 (1 - включительно, 2 - невключительно)
# L = 1 | R = 5
# prefix_sum[5] - prefix_sum[1] = 6 - 0 = 6



