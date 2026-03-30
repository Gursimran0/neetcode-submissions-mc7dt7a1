class Solution:
    def isPalindrome(self, s: str) -> bool:
        oldList = list(s)
        newList = []
        for i in range(len(oldList)):
            if oldList[i].isalnum():
                newList.append(oldList[i].lower())
        
        reversedList = newList[::-1]
            
        
        return newList == reversedList
