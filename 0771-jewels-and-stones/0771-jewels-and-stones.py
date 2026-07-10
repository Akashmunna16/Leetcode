class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        # Count stones that are in the jewel set
        return sum(stone in jewel_set for stone in stones)