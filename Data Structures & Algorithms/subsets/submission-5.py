class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(i,curr):
            if i>=len(nums):
                res.add(tuple(curr.copy()))
                return
            if i<=len(nums):
                res.add(tuple(curr.copy()))
            curr.append(nums[i])
            backtrack(i+1,curr)
            curr.pop()
            backtrack(i+1,curr)
        backtrack(0,[])
        return [list(elem) for elem in res]
        