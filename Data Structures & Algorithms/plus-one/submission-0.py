class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tempStr = ""
        for i in range(len(digits)):
            tempStr = tempStr + str(digits[i])
        tempInt = int(tempStr)+1

        return [int(x) for x in str(tempInt)]
        
        