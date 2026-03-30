class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnList = []
        for i in range(len(nums)):
            newTarget = target - nums[i]
            for j in range(len(nums)):
                if newTarget == nums[j] and i!=j:
                    returnList.append(i)
                    returnList.append(j)
                    return returnList
        return returnList
        