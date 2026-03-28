# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped: dict[tuple[str]] = {}
        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c)-ord("a")]+=1
            chars = tuple(chars)
            if chars not in grouped:
                grouped[chars] = []
            grouped[chars].append(s)
        return list(grouped.values())
