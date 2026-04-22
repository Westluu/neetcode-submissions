from collections import deque

class Solution:
    #Check each cell
    #if cell rotten
    #immediately mark adjacent cells as rotten (if they were fresh)
    #add converted fruit to skip hash
    #continue until end of grid

    #now we start at cells on the skip hash
    #repeat until there are no cell in the skip hash

    #once no cells in skip hash, check all for fresh fruit
    #if any fresh fruit then return -1
    #else return # of iterations


    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten_hash = set()
        next_rotten = set()
        minutes = 0

        def checkRotten(row, col):
            #check if ROTTEN
            if grid[row][col] == 2:
                #check if adjacent cell is a FF
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    #immediately mark adjacent cells as rotten (if they were fresh)
                    if (row + dr < 0 or col + dc < 0 or 
                        row + dr >= ROWS or col + dc >= COLS):
                        continue 

                    elif grid[row + dr][col + dc] == 1:
                        grid[row + dr][col + dc] = 2

                        #add converted fruit to skip hash
                        next_rotten.add((row + dr, col + dc))
                        print(next_rotten)
            return 

        #Minute 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in next_rotten:
                    checkRotten(row, col)
        rotten_hash = next_rotten.copy()
        next_rotten = set()

        #Check each rotten_hash
        while rotten_hash:
            for row, col in rotten_hash:
                checkRotten(row, col)
                print("after check: ", next_rotten)
            rotten_hash = next_rotten.copy()
            next_rotten = set()
            minutes += 1
        

        #final check
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    print(grid)
                    return -1

        print(grid)
        return minutes


#grid=[[2,1,1],[1,1,0],[0,1,1]]

            


