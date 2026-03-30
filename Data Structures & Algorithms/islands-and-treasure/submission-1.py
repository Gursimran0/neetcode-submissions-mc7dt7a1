class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()
        q=deque()

        def checkDist(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c]==-1:
                return
            q.append((r,c))
            seen.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
        dist = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                r,c = q.popleft()
                grid[r][c] = dist
                checkDist(r+1,c)
                checkDist(r-1,c)
                checkDist(r,c+1)
                checkDist(r,c-1)
            dist+=1
        