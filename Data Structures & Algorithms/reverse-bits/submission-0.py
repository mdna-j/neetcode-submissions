class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # Extract the LSB and shift it to its new reverse position
            ans |= (n & 1) << (31 - i)
            # Shift n to the right to process the next bit
            n >>= 1
        return ans