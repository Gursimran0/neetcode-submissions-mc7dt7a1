class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        def backtrack(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c] == "0":
                return
            seen.add((r,c))
            backtrack(r+1,c)
            backtrack(r-1,c)
            backtrack(r,c+1)
            backtrack(r,c-1)
        
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    total+=1
                    backtrack(r,c)
        return total
