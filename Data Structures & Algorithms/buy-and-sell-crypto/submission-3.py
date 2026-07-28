class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float('inf')
        
        for p in prices:
            if p < min_so_far:
                min_so_far = p
            elif p - min_so_far > max_profit:
                max_profit = p - min_so_far
                
        return max_profit