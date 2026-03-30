class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count ={}
        for elem in bills:
            if elem == 5:
                count[elem]=1+count.get(elem,0)
            elif elem == 10:
                if count.get(5,0)>=1:
                    count[5]-=1
                    count[elem]=1+count.get(elem,0)
                else:
                    return False
            elif elem == 20:
                if count.get(5,0)>=3:
                    count[5]-=3
                    count[elem]=1+count.get(elem,0)
                elif count.get(5,0)>=1 and count.get(10,0)>=1:
                    count[5]-=1
                    count[10]-=1
                    count[elem]=1+count.get(elem,0)
                else:
                    return False
        return True

            
