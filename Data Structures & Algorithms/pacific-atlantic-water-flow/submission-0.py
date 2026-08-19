class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #input: matrix of heights
        #output: A list of a cell that can flow to both pacific and alantic ocean

        #By definition a cell is able to flow to its adjacent cells if its val is 
        #equal or greater than its adjacent cells value

        #Thus for a cell to flow from both pacific and the alantic there must be 
        #a path such that the current cell value and its neighbors have values equal or greater

        #And if a cell is neighbors with a cell that has a flow path, and can flow to that neighbor 
        #then it must also mean the current cell can also flow to both paths

        #Thus intution using DFS to find if it can reach both
        
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        atlantic = set()
        pacific = set()
        res = []

        def dfs(r, c, ocean_vist, prev_height):
            if ((r,c) in ocean_vist or
                r >= ROWS or r < 0 or
                c >= COLS or c < 0 or
                heights[r][c] < prev_height
                ):
                return
            
            ocean_vist.add((r,c))
            for dr, dc in directions:
                dfs(dr+r, dc+c, ocean_vist, heights[r][c])
        

        #then start from ocean borders
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        
        return res

        



            




        