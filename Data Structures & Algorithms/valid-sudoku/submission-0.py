class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                entry = board[r][c]
                if entry == ".":
                    continue

                if entry in rows[r] or entry in columns[c] or entry in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(entry)
                columns[c].add(entry)
                squares[(r // 3, c // 3)].add(entry)
        return True

