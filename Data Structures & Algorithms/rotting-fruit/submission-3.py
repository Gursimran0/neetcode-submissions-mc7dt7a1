class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:

                    fresh+=1
                if grid[r][c] == 2:
                    seen.add((r,c))
                    q.append((r,c))
        def makeRotten(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0 or grid[r][c] == 2 or (r,c) in seen:
                return
            nonlocal fresh
            fresh -= 1
            seen.add((r,c))
            q.append((r,c))

        time = 0 
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                makeRotten(r+1,c)
                makeRotten(r-1,c)
                makeRotten(r,c+1)
                makeRotten(r,c-1)
            time+=1
        return time if fresh == 0 else -1