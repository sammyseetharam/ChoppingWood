class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific, atlantic = set(), set() 
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, setter, prev):
            if(r < 0 or r >= rows or c < 0 or c >= cols 
            or (r,c) in setter or prev > heights[r][c]):  
                return 
            
            setter.add((r,c))

            dfs(r + 1, c, setter, heights[r][c])
            dfs(r - 1, c, setter, heights[r][c])
            dfs(r, c + 1, setter, heights[r][c])
            dfs(r, c - 1, setter, heights[r][c])

        
        #go column wise 
        for c in range(cols): 
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        #go row wise
        for r in range(rows): 
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        #find the overlap between then 
        return [[r,c] for r in range(rows) for c in range(cols) if (r,c) in pacific and (r,c) in atlantic]

