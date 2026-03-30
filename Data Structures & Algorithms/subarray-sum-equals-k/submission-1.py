class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res = 0
        cSum = 0

        for elem in nums:
            cSum+= elem
            nSum = cSum - k
            
            if nSum in prefix.keys():
                res+= prefix[nSum]
            prefix[cSum] = 1+ prefix.get(cSum,0)
        return res
        