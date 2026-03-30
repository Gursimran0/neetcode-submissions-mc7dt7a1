class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                seen.add((r,c))
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    total+=1
                    dfs(r,c)
        return total

        