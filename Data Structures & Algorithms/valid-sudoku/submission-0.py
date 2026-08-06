class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}
        for r_idx, r_val in enumerate(board):
            for c_idx, c_val in enumerate(r_val):
                if c_val == '.':
                    continue

                if c_val in rows[r_idx]:
                    return False
                else:
                    rows[r_idx].add(c_val)
                
                if c_val in cols[c_idx]:
                    return False
                else:
                    cols[c_idx].add(c_val)
                
                key = (r_idx // 3, c_idx // 3)
                boxes.setdefault(key, set())

                if c_val in boxes[key]:
                    return False
                else:
                    boxes[key].add(c_val)
        return True