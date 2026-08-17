from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        visted = set()
        ROW = len(grid)
        COL = len(grid[0])
        
        #Find all treasures
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visted.add((r, c))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c
                if (new_r >= ROW or new_r < 0 or
                    new_c >= COL or new_c < 0 or
                    grid[new_r][new_c] == -1 or (new_r, new_c) in visted
                    ):
                    continue
                grid[new_r][new_c] =  grid[r][c] + 1
                queue.append((new_r, new_c))
                visted.add((new_r, new_c))
