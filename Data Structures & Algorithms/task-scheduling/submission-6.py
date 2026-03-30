class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        stack = []
        time = 0
        for val in count.values():
            stack.append(-val)
        heapq.heapify(stack)
        while stack or q:
            time+=1
            if stack:
                val = heapq.heappop(stack)
                val = val+1
                if val:
                    q.append((val,time+n))
            if q and q[0][1] == time:
                heapq.heappush(stack,q.popleft()[0])
            
        
        print(count)
        return time
        