class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        resSet = set(nums)
        count = 0

        for i in range(len(nums)):
            if nums[i]-1 in resSet:
                continue
            length = 1
            while nums[i]+length in resSet:
                length +=1
            count = max(count,length) 
        return count

        