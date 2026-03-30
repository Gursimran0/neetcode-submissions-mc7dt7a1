class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)-1
        
        low = 0
        high = length

        while low<=high:
            mid = (low + high)//2
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
            else:
                return mid

        return -1
        

