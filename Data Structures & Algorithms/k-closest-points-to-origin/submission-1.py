class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x,y in points:
            val = x**2 + y**2
            maxHeap.append([val,x,y])
        heapq.heapify(maxHeap)
        res = []
        while k>0:
            val,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
            k-=1
        return res

        