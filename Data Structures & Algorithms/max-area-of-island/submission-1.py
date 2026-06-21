class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #should be very similar to num islands but this time we keep track of a max 

        maxArea, area = 0, 0 
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        def dfs(r, c): 
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0: 
                return 0 

            grid[r][c] = 0
            total = 1
            for dx, dy in directions: 
                total += dfs(r + dx, c + dy) 
            
            return total 
            
            
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    area = dfs(r, c)
                    
                if area > maxArea: 
                    maxArea = area
        
        return maxArea
