class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        total = 0
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            
            findPrev = preSum -k
            total += count.get(findPrev,0)
            count[preSum] = 1 + count.get(preSum,0)
        return total
        