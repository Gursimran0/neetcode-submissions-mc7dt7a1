class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = []
        for i in range(len(nums)):
            if nums[i] in dupSet:
                return True
            
            dupSet.append(nums[i])
        return False
        