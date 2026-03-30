class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q= deque()
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def backtrack(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c] == -1:
                return
            q.append((r,c))
            seen.add((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    q.append((r,c))
        dist = 0 
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                backtrack(r+1,c)
                backtrack(r-1,c)
                backtrack(r,c+1)
                backtrack(r,c-1)
            dist+=1
        