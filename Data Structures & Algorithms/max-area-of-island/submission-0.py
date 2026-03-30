class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        if not grid:
            return 0
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(i,j):
            if i>=ROWS or j>=COLS or i<0 or j<0 or (i,j) in seen or grid[i][j] == 0:
                return
            seen.add((i,j))
            nonlocal total
            total +=1
            nonlocal res
            res = max(res,total)
            for r,c in directions:
                dfs(i+r,j+c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and not (r,c) in seen:
                    total = 0
                    dfs(r,c)
        return res

        