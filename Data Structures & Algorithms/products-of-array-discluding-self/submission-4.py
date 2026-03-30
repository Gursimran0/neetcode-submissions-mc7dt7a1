class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        result = [1] *l

        pre=1
        for i in range(l):
            result[i]=pre
            pre*=nums[i]
        post=1
        for i in range(l-1,-1,-1):
            result[i]*=post
            post*=nums[i]
        return result
 