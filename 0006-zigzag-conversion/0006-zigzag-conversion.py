class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base Case: If there's only 1 row or row count exceeds string size, layout doesn't change
        if numRows == 1 or numRows >= len(s):
            return s
            
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # Turn around when hitting the boundary rows
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            current_row += 1 if going_down else -1
            
        return "".join(rows)