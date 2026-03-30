class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        product = [1] * l
        prefix = [0] * l
        postfix = [0] * l
        prefix[0]=postfix[l-1]=1
        pre = 1
        for i in range(len(nums)):
            product[i]=(pre)
            pre *= nums[i]
        post=1
        for i in range(l-1,-1,-1):
            product[i]*=post
            post*=nums[i]
     
        return product