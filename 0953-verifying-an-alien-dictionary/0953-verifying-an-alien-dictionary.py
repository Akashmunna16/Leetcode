class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary to map each letter to its index in the alien alphabet
        order_map = {char: idx for idx, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            # Compare the two words letter by letter
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # If characters differ, verify if they match the required order
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                # If loop finishes without breaking, check for prefix length violations
                if len(w1) > len(w2):
                    return False
                    
        return True