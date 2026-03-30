class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)

        i=0
        while i in seen:
            i+=1
        return i