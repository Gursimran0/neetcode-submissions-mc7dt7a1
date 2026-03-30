class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElement = math.ceil(len(nums) / 2)
        count = {}
        for elem in nums:
            count[elem] = 1 + count.get(elem,0)
        for num,cnt in count.items():
            if cnt>=majElement:
                return num
        