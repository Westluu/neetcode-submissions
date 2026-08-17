class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        max_area = 0

        def dfs(r, c):
            if r >= ROW or r < 0 or c >= COL or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area=1

            for dr, dc in directions:
                area+=dfs(r+dr, c+dc)

            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area


        


        