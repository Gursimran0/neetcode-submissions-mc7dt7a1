class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            revisedTarget = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == revisedTarget:
                    result.append(i)
                    result.append(j)
        return result