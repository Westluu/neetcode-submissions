class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTION = DIRECTION = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    #RIGHT, LEFT, UP, DOWN
        max_area = 0
        area = 0

        def dfs(r, c):
            nonlocal area
            if (min(r,c) < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0):
                return 
            
            grid[r][c] = 0
            area += 1

            for dr, dc in DIRECTION:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, area)
                    area = 0
        
        return max_area



        