class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [0] * (len(nums))
        after = [0] * (len(nums))
        res = [0] * (len(nums))

        prev[0] = after[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prev[i] = nums[i-1] * prev[i-1]
        print(prev)
        for i in range(len(nums)-2,-1,-1):
            after[i] = nums[i+1] * after[i+1]
        print(after)
        for i in range(len(nums)):
            res[i] = prev[i] * after[i]
        return res
        