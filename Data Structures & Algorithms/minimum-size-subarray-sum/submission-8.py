class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res = float("infinity")
        total = 0
        count = 0
        for r in range(len(nums)):
            total+=nums[r]
            
            while total>=target:
                res = min(res,r-l+1)
                
                total-=nums[l]
                l+=1
                
        return res if res!=float("infinity") else 0