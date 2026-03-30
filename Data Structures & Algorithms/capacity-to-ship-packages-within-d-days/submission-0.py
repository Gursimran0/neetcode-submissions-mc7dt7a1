class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            ship= 1
            currCap = cap
            for weight in weights:
                if currCap - weight<0:
                    ship+=1
                    if ship>days:
                        return False
                    currCap = cap
                currCap -=weight
            return True
        l=max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            m = (l+r)//2
            if canShip(m):
                res = min(res,m)
                r=m-1
            else:
                l = m+1
        return res

        
        

        