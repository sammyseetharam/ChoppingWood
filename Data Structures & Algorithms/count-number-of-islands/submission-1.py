class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #need to look up and down, left and right 
        #keep track of islands found in a outside variable 

        islands = 0 #counter 
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], #left
                       [1, 0], #right 
                       [0, -1], #up 
                       [0, 1]]  #down 

        def dfs(r, c):
            #out of bounds/water case 
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0": 
                return 

            grid[r][c] = "0"  #dont we want to reset the current to 0? 
            #if it gets here its at least one island 
            for dx, dy in directions: 
                dfs(r + dx, c + dy) #move on direction wise 
        
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1": 
                    dfs(r, c)
                    islands += 1
                            
        return islands
