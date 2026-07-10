from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Clean license plate and get letter frequencies
        plate_letters = [char.lower() for char in licensePlate if char.isalpha()]
        plate_count = Counter(plate_letters)
        
        shortest_word = None
        
        for word in words:
            word_count = Counter(word)
            
            # Check if word contains all required license plate letters with sufficient counts
            if all(word_count[char] >= plate_count[char] for char in plate_count):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
                    
        return shortest_word