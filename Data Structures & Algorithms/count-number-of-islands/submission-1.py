class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        islands = 0
        DIRECTION = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    #RIGHT, LEFT, UP, DOWN

        def dfs(r, c):
            
            # if we hit water or out of bounds
            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or 
                grid[r][c] == "0"):
                return
            
            grid[r][c] = "0" #make cur as visted
            for dr, dc in DIRECTION:
                dfs(r + dr, c + dc)

        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
            



            

            
        

        