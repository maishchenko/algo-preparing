# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"

class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split(" ")
        for i, word in enumerate(splitted):
            splitted[i] = word[::-1]
        return " ".join(splitted)
        
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseWords(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert sol.reverseWords(s="Mr Ding") == "rM gniD"