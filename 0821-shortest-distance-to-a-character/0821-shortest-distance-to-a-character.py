class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n
        
        # Pass 1: Left to Right sweep
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
            
        # Pass 2: Right to Left sweep
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
            
        return ans