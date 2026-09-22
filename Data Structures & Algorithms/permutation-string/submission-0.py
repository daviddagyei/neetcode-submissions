class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        curr_window = {}

        for i in range(len(s1)):
            target[s1[i]] = target.get(s1[i], 0) + 1
            curr_window[s2[i]] = curr_window.get(s2[i], 0) + 1
        
        if curr_window == target:
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            curr_window[s2[right]] = curr_window.get(s2[right], 0) + 1

            curr_char = s2[left]
            curr_window[curr_char] -= 1

            if curr_window[curr_char] == 0:
                del curr_window[curr_char]
            
            left += 1

            if curr_window == target:
                return True

        return False