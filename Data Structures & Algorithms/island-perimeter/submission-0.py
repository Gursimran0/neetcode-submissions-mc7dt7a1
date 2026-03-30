class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def backtrack(i,j):
            if i >=ROWS or j>=COLS or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in seen :
                return 0
            seen.add((i,j))
            peri = backtrack(i-1,j)
            peri += backtrack(i+1,j)
            peri += backtrack(i,j-1)
            peri += backtrack(i,j+1)
            return peri
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return backtrack(i,j)
            


        