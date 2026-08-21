class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        n_squared = n * n
        
        # Track frequency of each number
        cnt = [0] * (n_squared + 1)
        
        for row in grid:
            for num in row:
                cnt[num] += 1
                
        repeated = -1
        missing = -1
        
        # Find which number is repeated (count == 2) and missing (count == 0)
        for i in range(1, n_squared + 1):
            if cnt[i] == 2:
                repeated = i
            elif cnt[i] == 0:
                missing = i
                
        return [repeated, missing]
