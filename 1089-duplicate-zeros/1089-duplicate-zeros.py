class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)
        
        # Iterate backwards from virtual expanded index space
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0