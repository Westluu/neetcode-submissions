from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        fresh = 0
        ROW = len(grid)
        COL = len(grid[0])

        #Add all rotten fruits to the queue
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh+=1
        
        #start rot spreading
        minute = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    new_r = dr + r
                    new_c = dc + c

                    if (new_r >= ROW or new_r < 0 or
                        new_c >= COL or new_c < 0 or 
                        grid[new_r][new_c] == 0):
                        continue

                    if grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        fresh-=1
            minute+=1
        
        if fresh:
            return -1
        return minute
                