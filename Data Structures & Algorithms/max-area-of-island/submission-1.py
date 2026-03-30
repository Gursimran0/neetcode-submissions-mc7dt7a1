class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res= 0
        ROWS = len(grid)
        COLS =  len(grid[0])
        seen = set()

        def totalArea(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c] == 0:
                return
            seen.add((r,c))
            nonlocal total
            total+=1
            nonlocal res
            res = max(total,res)
            totalArea(r+1,c)
            totalArea(r-1,c)
            totalArea(r,c+1)
            totalArea(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                total = 0
                if grid[r][c] == 1 and (r,c) not in seen:
                    totalArea(r,c)
                    res = max(res, total)
                    
        return res