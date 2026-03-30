class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()
        
        def totalArea(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c] == 0:
                return
            nonlocal area 
            seen.add((r,c))
            area +=1
            totalArea(r+1,c)
            totalArea(r-1,c)
            totalArea(r,c+1)
            totalArea(r,c-1)
            nonlocal res
            res = max(res,area)

        for r in range(ROWS):
            for c in range(COLS):
                area = 0
                if (r,c) not in seen and grid[r][c] == 1:
                    totalArea(r,c)
                    
        return res

