class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        def backtrack(i,r,c):
            if len(word) == i:
                return True
            if i>len(word) or r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] != word[i] or (r,c) in seen:
                return False
            seen.add((r,c))
            res = backtrack(i+1,r+1,c) or backtrack(i+1,r-1,c) or backtrack(i+1,r,c+1) or backtrack(i+1,r,c-1)
            seen.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0,r,c):
                    return True
        return False



        