class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                box_index = ((row//3)*3 + col//3)

                if num == ".":
                    continue
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in boxes[box_index]:
                    return False
                
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)
        return True
        