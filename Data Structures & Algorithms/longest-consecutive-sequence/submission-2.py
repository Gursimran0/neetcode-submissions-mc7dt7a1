class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 in numSet:
                continue
            count =1
            x=nums[i]
            while x+1 in numSet :
                count +=1
                x+=1
            longest = max(longest,count)
        return longest