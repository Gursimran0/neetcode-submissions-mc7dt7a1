class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()

        q=deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    q.append((r,c))
        
        def addCell(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c] == -1:
                return
            seen.add((r,c))
            q.append((r,c))

        dist = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                r,c = q.popleft()
                grid[r][c] = dist
                
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            dist+=1

        