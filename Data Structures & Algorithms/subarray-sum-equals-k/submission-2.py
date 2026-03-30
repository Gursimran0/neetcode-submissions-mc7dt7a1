class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res = 0
        nSum = 0
        for i in range(len(nums)):
            nSum += nums[i]
            cSum = nSum - k
            if cSum in prefix.keys():
                res +=prefix[cSum]
            prefix[nSum] = 1+prefix.get(nSum,0)
        return res
        