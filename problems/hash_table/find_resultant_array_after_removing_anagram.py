# 2273. Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/

# Example 1:
# Input: words = ["abba","baba","bbaa","cd","cd"]
# Output: ["abba","cd"]

# Input: words = ["a","b","c","d","e"]
# Output: ["a","b","c","d","e"]`

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        return result
    

if __name__ == "__main__":
    sol = Solution()
    assert sol.removeAnagrams(["abba","baba","bbaa","cd","cd"]) == ["abba","cd"]
    assert sol.removeAnagrams(["a","b","c","d","e"]) == ["a","b","c","d","e"]
    