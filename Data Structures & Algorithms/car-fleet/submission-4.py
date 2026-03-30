class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        for i in range(len(position)):
            res.append((position[i],speed[i]))
        
        stack = []
        res.sort(reverse=True)
        for i in range(len(res)):
            time = (target-res[i][0])/res[i][1]
            stack.append(time)
            while len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
             
         
        