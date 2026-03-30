class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def backtrack(i,curr):
            if i==len(nums):
                res.append(curr.copy())
                return

            if i>len(nums) or len(curr)>len(nums):
                return
            curr.append(nums[i])
            backtrack(i+1,curr)
            curr.pop()
            backtrack(i+1,curr)
        backtrack(0,curr)
        return res    
        