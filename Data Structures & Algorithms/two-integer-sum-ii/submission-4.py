class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        for i, num in enumerate(numbers):
            rem  = target - num
            if rem in numbers[i+1 :]:
                res.append(i + 1)
                res.append(numbers[i+1 :].index(rem) + 2 + i)
                return res
        
        

        