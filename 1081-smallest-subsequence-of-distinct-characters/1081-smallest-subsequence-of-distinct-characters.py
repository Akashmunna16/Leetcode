class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Map each character to its last occurrence index position
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        stack = []
        seen = set()  # Keeps track of characters currently inside the stack
        
        # Step 2: Build the lexicographically smallest subsequence
        for idx, char in enumerate(s):
            # If the character is already inside the stack, skip it
            if char in seen:
                continue
                
            # Evict larger characters from the stack if they appear again later
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Push the current character onto the stack
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)