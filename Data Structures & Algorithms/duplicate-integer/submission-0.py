class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = []
        for i in nums:
            if i not in newList:
                newList.append(i)
            else:
                return True
        return False
         