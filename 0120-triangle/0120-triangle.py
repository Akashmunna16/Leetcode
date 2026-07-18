class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Initialize DP row using the bottom layer of the triangle
        dp = triangle[-1]
        
        # Bottom-up evaluation starting from the second-to-last row
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                # Update choice: current cell value + min of the two reachable lower choices
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
                
        return dp[0]