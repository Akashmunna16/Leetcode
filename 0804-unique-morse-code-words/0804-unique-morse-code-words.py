class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
                 
        unique_transforms = set()
        
        for word in words:
            # Map each character to its Morse equivalent and join them
            transformation = "".join(MORSE[ord(char) - 97] for char in word)
            unique_transforms.add(transformation)
            
        return len(unique_transforms)