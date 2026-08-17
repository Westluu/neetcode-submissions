class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def dfs(r, c):
            if r >= ROW or r < 0 or c >= COL or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1
        
        return islands



                
            

        
        
        