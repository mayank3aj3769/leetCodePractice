class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        cell=collections.defaultdict(set)
         
        ## use 3 hashsets to solve . Also see the syntax of hashsets

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c]=='.':
                    continue
                if ( (board[r][c] in row[r]) or (board[r][c] in col[c]) or (board[r][c] in cell[(r//3,c//3)])):
                    return False
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                cell[(r//3,c//3)].add(board[r][c])
        
        return True