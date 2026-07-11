class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n != 1 and n not in visited:
            visited.add(n)
            
            # Sum of squares of digits
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n = n // 10
            
            n = sum_of_squares
            
        return n == 1