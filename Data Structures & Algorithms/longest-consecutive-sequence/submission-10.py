class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        seen=set(nums)
        res=1
        for elem in nums:
            if elem-1 in seen:
                continue
            length = 1
            while elem +length in seen:
                length +=1
                res= max(length,res)
        
        return res
        