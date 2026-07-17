class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        nums.sort()

        res = []


        for i, num in enumerate(nums):
            if i > 0  and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == (-num):
                    res.append([nums[left], nums[right], num])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                elif nums[left] + nums[right] > (-num):
                    right -= 1
                
                elif nums[left] + nums[right] < (-num):
                    left += 1
                
            
                
        
        return res

        