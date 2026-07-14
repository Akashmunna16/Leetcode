class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_path):
            # Base Case: If the path matches the input length
            if len(current_path) == len(digits):
                result.append("".join(current_path))
                return
                
            # Fetch letters corresponding to the current digit index position
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                current_path.append(letter)       # Choose
                backtrack(index + 1, current_path) # Recurse
                current_path.pop()                 # Backtrack
                
        backtrack(0, [])
        return result