class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,perm = [],[]
        n = len(nums)

        def backtrack():
            if len(perm)==n:
                res.append(perm.copy())
                return
            
            for i in nums:
                if i not in perm:
                    perm.append(i)
                    backtrack()
                    perm.pop()
                    
        backtrack()
        return res
                