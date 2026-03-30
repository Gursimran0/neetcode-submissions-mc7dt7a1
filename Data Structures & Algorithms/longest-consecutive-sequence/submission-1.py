class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in numSet:
                count = 1
                while nums[i]+count in numSet:
                    count+=1
                longest = max(count,longest)

        return longest  