class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append((position[i],speed[i]))
        posSpeed.sort(reverse=True)
        for i in range(len(posSpeed)):
            time = (target-posSpeed[i][0])/posSpeed[i][1]
            res.append(time)
            if len(res)>=2 and res[-1]<=res[-2]:
                res.pop()
        return len(res)