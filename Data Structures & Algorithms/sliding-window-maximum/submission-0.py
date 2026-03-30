class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0 
        r = k
        for r in range(r,len(nums)+1):
            newArray = nums[l:r]
            print(newArray)
            res.append(max(newArray))
            l+=1
        return res
        