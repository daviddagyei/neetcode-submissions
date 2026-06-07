class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i, num in enumerate(nums):
            curr_res = 1
            curr = nums[:i] + nums[i+1:]

            for j in curr:
                curr_res *= j

            res[i] *= curr_res

        return res



        