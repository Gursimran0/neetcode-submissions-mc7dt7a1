class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        if not grid:
            return 0
        seen = set()
        def dfs(i,j):
            if i>=ROWS or j>=COLS or i<0 or j<0 or (i,j) in seen or grid[i][j] == "0":
                return
            
            seen.add((i,j))
            for c,r in directions:
                dfs(i+c,j+r)
        totalIslands = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and not (r,c) in seen:
                    totalIslands += 1
                    dfs(r,c)
        return totalIslands       
        
        