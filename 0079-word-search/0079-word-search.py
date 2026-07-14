class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, index):
            # Base Case: All characters matched
            if index == len(word):
                return True
                
            # Out of bounds or mismatch checks
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[index]):
                return False
                
            # Mark the cell as visited during this path branch
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all four adjacent directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
                     
            # Backtrack: Restore the cell value
            board[r][c] = temp
            return found

        # Search the grid for the starting point
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False