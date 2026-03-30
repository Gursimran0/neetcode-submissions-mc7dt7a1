class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        
        res = 0
        for elem in nums:
            if elem-1 in seen:
                continue
            l=1
            while elem +l in seen:
                l+=1
            res = max(res,l)
        return res

        