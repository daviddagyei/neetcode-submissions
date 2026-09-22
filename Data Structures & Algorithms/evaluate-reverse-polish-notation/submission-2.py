class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "*", "-", "/"}
        nums = []
        curr = 0
        for char in tokens:
            if char not in operators:
                nums.append(int(char))
            else:
                right = nums.pop()
                left = nums.pop()
                if char == "+":
                    curr = left + right
                elif char == "-":
                    curr = left - right
                elif char == "*":
                    curr = left * right
                else:
                    curr = int(left/right)
                
                nums.append(curr)
        
        return nums.pop()

        





        