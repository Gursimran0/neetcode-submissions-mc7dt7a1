class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        print(nums)
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        print(nums)
        return nums[0]
        