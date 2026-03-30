class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(len(nums)):
            prod = 1
            for j in range(0,len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            product.append(prod)
        return product