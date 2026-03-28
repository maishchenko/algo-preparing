# 748. Shortest Completing Word
# https://leetcode.com/problems/shortest-completing-word/description/
#
# Example 1
# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.
# 
# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', 
# but among these "pest", "stew", and "show" are shortest. 
# The answer is "pest" because it is the word that appears earliest of the 3.


from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(c.lower() for c in licensePlate if c.isalpha())
        result = None
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] >= need[c] for c in need):
                if result is None or len(word) < len(result):
                    result = word
        return result
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.shortestCompletingWord(
        licensePlate="1s3 PSt",
        words=["step","steps","stripe","stepple"]
    ) == "steps"

    assert sol.shortestCompletingWord(
        licensePlate = "1s3 456", 
        words = ["looks","pest","stew","show"]
    ) == "pest"
    