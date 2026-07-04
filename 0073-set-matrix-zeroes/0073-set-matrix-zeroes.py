class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Step 1: Determine if first row or first col need to be zeroed out
        for c in range(cols):
            if matrix[0][c] == 0: first_row_zero = True
        for r in range(rows):
            if matrix[r][0] == 0: first_col_zero = True
            
        # Step 2: Use first row/col as marker stores for the rest of the grid
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    
        # Step 3: Apply zeroes based on those stored markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # Step 4: Separately zero out the first row and first column if needed
        if first_row_zero:
            for c in range(cols): matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows): matrix[r][0] = 0