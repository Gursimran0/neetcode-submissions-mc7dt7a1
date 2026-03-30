class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        n = len(nums)

        pre = 1
        pos = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        for j in range(n-1,-1,-1):
            res[j]*=pos
            pos*=nums[j]
        print(res)
        return res
        