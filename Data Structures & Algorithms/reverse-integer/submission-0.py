class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of the integer
        sign = -1 if x < 0 else 1
        
        # Reverse the absolute value using string slicing
        reversed_int = int(str(abs(x))[::-1])
        
        # Apply the original sign
        result = sign * reversed_int
        
        # Check for 32-bit signed integer overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result
        