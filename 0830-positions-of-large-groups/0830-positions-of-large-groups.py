class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        i = 0  # Start index of the current group
        n = len(s)
        
        for j in range(n):
            # Run breaks if we hit a new character or reach the end of the string
            if j == n - 1 or s[j] != s[j + 1]:
                # If the current consecutive block length is 3 or more
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1  # Reset start tracking index to the next group
                
        return ans