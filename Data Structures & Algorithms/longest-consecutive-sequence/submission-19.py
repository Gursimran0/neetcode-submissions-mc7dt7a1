class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for elem in nums:
            if elem-1 not in seen:
                count = 1
                while elem+1 in seen:
                    count+=1
                    elem+=1
                res=max(res,count)
        return res

        