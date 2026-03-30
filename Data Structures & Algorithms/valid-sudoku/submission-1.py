from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_sets, col_sets, chunks = [set() for _ in range(n)], [set() for _ in range(n)], [[set()for _ in range(3)] for _ in range(3)]
        for row_i, row in enumerate(board):
            for col_i, cell in enumerate(row):
                if cell != '.':
                    # check row
                    if cell not in row_sets[row_i]:
                        row_sets[row_i].add(cell)
                    else:
                        return False
                    # check col
                    if cell not in col_sets[col_i]:
                        col_sets[col_i].add(cell)
                    else:
                        return False
                    # check chunk
                    chunk_row_i, chunk_col_i = row_i//3, col_i//3
                    if cell not in chunks[chunk_row_i][chunk_col_i]:
                        chunks[chunk_row_i][chunk_col_i].add(cell)
                    else:
                        return False
        return True
