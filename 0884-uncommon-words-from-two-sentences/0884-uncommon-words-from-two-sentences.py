from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences and combine into a single list of tokens
        words = s1.split() + s2.split()
        
        # Count the frequency of every word across both sentences
        counts = Counter(words)
        
        # A word is uncommon if its total global frequency count is exactly 1
        return [word for word in counts if counts[word] == 1]