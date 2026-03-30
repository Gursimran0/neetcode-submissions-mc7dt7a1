class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        numbers.sort()
        l=0
        r=len(numbers)-1

        while l<r:
            newTarget = numbers[r] + numbers[l]
            if newTarget> target:
                r-=1
            elif newTarget<target:
                l+=1
            else:
                return [l+1,r+1]

        