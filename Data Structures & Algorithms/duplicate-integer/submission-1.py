class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = []
        for i in range(len(nums)):
            if nums[i] in setList:
                return True
            else:
                setList.append(nums[i])
        return False

        