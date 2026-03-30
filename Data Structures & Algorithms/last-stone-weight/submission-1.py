class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones)>1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a == b:
                continue
            elif a<b:
                c=b-a
                heapq.heappush(stones,-c)
            else:
                c=a-b
                heapq.heappush(stones,-c)
        if stones:
            return -stones[0]
        return 0
        