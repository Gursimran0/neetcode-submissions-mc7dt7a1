class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for elem in nums:
            if elem-1 not in numSet:
                length = 1
                while (elem+length) in numSet:
                    length +=1
                longest = max(length,longest)
        return longest


        

        
        