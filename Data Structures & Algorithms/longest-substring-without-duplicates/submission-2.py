from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        seen = set()
        max_length = 0

        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                if r - l > max_length:
                    max_length = r - l
   
            else:
                seen.remove(s[l])
                l += 1 

        return max_length






