# 415. Add Strings
# https://leetcode.com/problems/add-strings/description/

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        n, m = len(num1) - 1, len(num2) - 1
        carry = 0
        while n >= 0 and m >= 0:
            total = int(num1[n]) + int(num2[m]) + carry # ord(num1[n]) - ord('0')
            result.append(str(total % 10))
            carry = total // 10
            n -= 1
            m -= 1
        while n >= 0:
            total = int(num1[n]) + carry 
            result.append(str(total % 10))
            carry = total // 10
            n -= 1   
        while m >= 0:
            total = int(num2[m]) + carry
            result.append(str(total % 10))
            carry = total // 10
            m -= 1     
        if carry != 0:
            result.append(str(carry))  
        return "".join(result[::-1])
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.addStrings(num1 = "11", num2 = "123") == "134"
