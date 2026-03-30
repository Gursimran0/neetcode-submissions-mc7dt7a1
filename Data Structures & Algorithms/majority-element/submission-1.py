import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate)> (l//2):
                return candidate
        

        