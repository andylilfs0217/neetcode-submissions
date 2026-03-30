class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_nums = [set() for _ in range(n)]
        col_nums = [set() for _ in range(n)]
        grid_nums = [[set() for _ in range(n//3)] for _ in range(n//3)]

        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell != '.':
                    if cell in row_nums[row_idx] or \
                        cell in col_nums[col_idx] or \
                        cell in grid_nums[row_idx//3][col_idx//3]:
                        return False

                    row_nums[row_idx].add(cell)
                    col_nums[col_idx].add(cell)
                    grid_nums[row_idx//3][col_idx//3].add(cell)
        return True