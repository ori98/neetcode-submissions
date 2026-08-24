from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash_set = defaultdict(set)
        col_hash_set = defaultdict(set)
        sq_hash_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]

                if curr_val == ".":
                    # skip
                    continue
                
                if (curr_val in row_hash_set[r] or
                curr_val in col_hash_set[c] or
                curr_val in sq_hash_set[(r//3, c//3)]):
                    return False
                
                # add the values
                row_hash_set[r].add(curr_val)
                col_hash_set[c].add(curr_val)
                sq_hash_set[(r//3, c//3)].add(curr_val)
        
        return True
