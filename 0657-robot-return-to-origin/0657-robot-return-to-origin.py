class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Verify vertical and horizontal movements balance out to 0
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')