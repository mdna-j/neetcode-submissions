class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1 
        
        for i in range(1, n + 1):
            # When i hits the next power of 2, update offset
            if offset * 2 == i:
                offset = i
            # i = offset (leading 1) + remainder (i - offset)
            # So bit count = 1 + bit count of remainder
            dp[i] = 1 + dp[i - offset]
        
        return dp
        