class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Calculate effective shifts needed
        k %= total
        if k == 0:
            return grid
            
        # Create a blank target grid of the same dimensions
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # 1. Convert current (r, c) to 1D index
                old_1d_idx = r * n + c
                
                # 2. Shift the 1D index forward with wrap-around
                new_1d_idx = (old_1d_idx + k) % total
                
                # 3. Convert new 1D index back to 2D coordinates
                new_r = new_1d_idx // n
                new_c = new_1d_idx % n
                
                # Place element in the target position
                result[new_r][new_c] = grid[r][c]
                
        return result