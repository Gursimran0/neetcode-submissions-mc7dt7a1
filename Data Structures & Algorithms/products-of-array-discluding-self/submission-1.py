class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        product = [0] * l
        prefix = [0] * l
        postfix = [0] * l
        prefix[0]=postfix[l-1]=1
        for i in range(1,len(nums)):
           prefix[i] = prefix[i-1] *nums[i-1]
        for i in range(l-2,-1,-1):
            postfix[i] = nums[i+1] * postfix[i+1]
        for i in range(len(product)):
            product[i] = prefix[i] * postfix[i]
        return product