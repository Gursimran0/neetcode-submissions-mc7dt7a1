class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for elem in nums:
                if elem not in perm:
                    perm.append(elem)
                    backtrack()
                    perm.remove(elem)
        backtrack()
        return res
        