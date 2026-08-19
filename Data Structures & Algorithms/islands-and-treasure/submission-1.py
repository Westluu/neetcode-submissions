from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #the idea is to find a treasures
        #from the teasures run BFS to compute the shortest path to INF states
        #skipping -1 States
        #keeping the min distance

        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        visted = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visted.add((r,c))
        
        while queue:
            r,c = queue.popleft()
            
            for dr, dc in directions:
                new_r = dr+r
                new_c = dc+c
                if (new_r >= ROWS or new_r < 0 or
                    new_c >= COLS or new_c < 0 or
                    grid[new_r][new_c] == -1 or (new_r,new_c) in visted):
                    continue

                grid[new_r][new_c] = min(grid[r][c] + 1, grid[new_r][new_c])
                queue.append((new_r, new_c))
                visted.add((new_r,new_c))

        

        