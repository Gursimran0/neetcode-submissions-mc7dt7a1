class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        seen = set()
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    q.append((r,c))
        
                if grid[r][c] == 1:
                    fresh+=1
        time = 0
        while q and fresh>0:
            qLen = len(q)
            for i in range(qLen):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row<0 or col<0 or row>=ROWS or col>=COLS or (row,col) in seen or grid[row][col]!=1:
                        continue
                    grid[row][col] = 2
                    fresh-=1
                
                    q.append((row,col))
            time+=1
        return time if fresh == 0 else -1
        
        