class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All caps
        # Case 2: All lowercase
        # Case 3: Title Case (First letter capital, rest lowercase)
        return word.isupper() or word.islower() or word.istitle()