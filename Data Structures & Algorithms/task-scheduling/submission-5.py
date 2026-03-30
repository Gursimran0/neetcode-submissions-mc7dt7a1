class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q=deque() #(task,time)
        minHeap = []
        count = Counter(tasks)
        for val in count.values():
            minHeap.append(-val)
        time=0
        heapq.heapify(minHeap)
        while minHeap or q:
            time+=1
            if minHeap:
                cnt = 1+heapq.heappop(minHeap)
                if cnt:
                    q.append((cnt,time+n))
            if q and q[0][1] == time:
                heapq.heappush(minHeap,q.popleft()[0])
        return time
        