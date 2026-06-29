class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        

        #within this function, we check out of bounds, edges, or being an X and then breakout
        #else we're good, to replace 
        def dfs(r, c):
            if (r < 0 or r >= rows - 1  or c < 0 or c >= cols - 1 or board[r][c] == 'X'):
                return 

            board[r][c] = "X"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows): 
            for c in range(cols): 
                if(board[r][c] == "O"):   
                    dfs(r, c)
        
        return 