class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float('inf')

        for p in prices:
            if p < min_so_far:
                min_so_far = p
            
            if p > min_so_far:
                curr = p - min_so_far
                max_profit = max(max_profit, curr)

        return max_profit





        