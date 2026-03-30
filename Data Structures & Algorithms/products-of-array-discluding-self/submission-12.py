class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0]*l
        pre = 1
        pos = 1

        for i in range(l):
            res[i] = pre
            pre  *= nums[i]
        for i in range(l-1,-1,-1):
            res[i]*=pos
            pos  *= nums[i]
        return res
        