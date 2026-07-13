class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            # Check the memoization state cache
            if (i, j) in memo:
                return memo[(i, j)]
                
            # Base Case: Pattern fully processed
            if j == len(p):
                return i == len(s)
                
            # Check if current characters align or hit a '.' wildcard
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # If the next token is a '*' repeat modifier
            if j + 1 < len(p) and p[j + 1] == '*':
                # Choice 1: Ignore the '*' rule (match 0 times)
                # Choice 2: Consume 1 character from s (if first_match is True) and keep pattern state active
                ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # Normal structural forward shift step
                ans = first_match and dfs(i + 1, j + 1)
                
            memo[(i, j)] = ans
            return ans
            
        return dfs(0, 0)