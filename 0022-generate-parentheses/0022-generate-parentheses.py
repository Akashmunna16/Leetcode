class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(left_count, right_count, current_path):
            # Base Case: Path length reaches the target combinations boundary limit
            if len(current_path) == 2 * n:
                result.append("".join(current_path))
                return
                
            # Rule 1: We can always add a '(' if we haven't reached the limit n
            if left_count < n:
                current_path.append('(')
                backtrack(left_count + 1, right_count, current_path)
                current_path.pop()
                
            # Rule 2: We can only add a ')' if it balances an existing unmatched '('
            if right_count < left_count:
                current_path.append(')')
                backtrack(left_count, right_count + 1, current_path)
                current_path.pop()
                
        backtrack(0, 0, [])
        return result