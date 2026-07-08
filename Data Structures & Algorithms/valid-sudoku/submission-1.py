class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        row_set = [set() for i in range(n)]
        col_set = [set() for i in range(n)]
        subgrid_set = [[set() for i in range(n)] for j in range(n) ]

        for r in range(n):
            for c in range(n):
                cell = board[r][c]
                if cell == ".":
                    continue
                
                if cell in row_set[r]:
                    return False
                if cell in col_set[c]:
                    return False
                if cell in subgrid_set[r // 3][c//3]:
                    return False
                
                row_set[r].add(cell)
                col_set[c].add(cell)
                subgrid_set[r//3][c//3].add(cell)

        return True



        
        