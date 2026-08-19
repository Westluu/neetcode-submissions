from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #region is 0 connected, can have any shape and regions are
        #connected if its neighbors are also 0s

        #A region is surrounded is none of its 0 cells touches a border of the board
        #Where regions are enclosed by X cells arounds its perimeter

        #intutions look for all O cells, and from there check if that 0 cell is part of a region
        #once done, done while searching if any of that cell touches the border, dont capture it
        #if does not capture it by turning it all to X

        queue = deque()
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        visted = set()

        #LEFT & RIGHT EDGE
        for r in range(ROWS):
            if board[r][0] == "O":
                queue.append((r,0))
                visted.add((r,0))
            if board[r][COLS-1] == "O":
                queue.append((r, COLS-1))
                visted.add((r,COLS-1))

        #TOP & BOTTOM EDGE
        for c in range(COLS):
            if board[0][c] == "O":
                queue.append((0,c))
                visted.add((0,c))
            if board[ROWS-1][c] == "O":
                queue.append((ROWS-1, c))
                visted.add((ROWS-1,c))
        
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c

                if (new_r >= ROWS or new_r < 0 or
                    new_c >= COLS or new_c < 0 or
                    board[new_r][new_c] == "X" or (new_r, new_c) in visted
                    ):
                    continue

                visted.add((new_r, new_c))
                queue.append((new_r, new_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visted:
                    board[r][c] = "X"




        