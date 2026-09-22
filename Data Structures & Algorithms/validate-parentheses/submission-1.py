class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stk = []

        for char in s:
            if char not in pairs:
                stk.append(char)
            
            else:
                if not stk:
                    return False

                last = stk[-1]
                if pairs[char] != last:
                    return False
                stk.pop()

        return len(stk) == 0


