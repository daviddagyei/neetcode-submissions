class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
            
        result = sorted(seen.items(), key=lambda x: x[1])
        res = result[len(result) - k :len(result)]
        ans = []
        for k, v in res:
            ans.append(k)

        return ans
 


        
        