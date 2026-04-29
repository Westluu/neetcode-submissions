class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                #skip starting point
                if i == j == 0:
                    continue

                left = up = float('inf')
                if i != 0: #we can check prev path up
                    up = grid[i - 1][j] + grid[i][j]
                if j != 0: #we can check prev path left
                    left = grid[i][j - 1] + grid[i][j]

                grid[i][j] = min(left, up)
        
        return grid[ROWS - 1][COLS - 1]