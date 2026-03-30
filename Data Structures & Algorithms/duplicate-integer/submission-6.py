class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()
        for i in range(len(nums)):
            if nums[i] in dupSet:
                return True
            
            dupSet.add(nums[i])
        return False
        