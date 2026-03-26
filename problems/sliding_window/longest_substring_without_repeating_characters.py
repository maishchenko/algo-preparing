import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start, end = 0, 0
        chars_dict = collections.defaultdict(int)
        max_length = 0
        for end in range(len(s)):
            char = s[end]
            chars_dict[char] += 1
            while chars_dict[char] > 1:
                char_to_del = s[start]
                chars_dict[char_to_del] -= 1
                if chars_dict[char_to_del] == 0:
                    del chars_dict[char_to_del]
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
            
            
if __name__ == "__main__":
    s = "abcabba"
    sol = Solution()
    count = sol.lengthOfLongestSubstring(s)
    print(count)
