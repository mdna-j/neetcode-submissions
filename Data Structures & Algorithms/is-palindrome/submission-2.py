class Solution:
    def isPalindrome(self, s: str) -> bool:
        # String S, returns true if its a isPalindrome
        cleaned = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(cleaned) - 1

        # otherwise returns false
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False

            l += 1
            r -= 1
        return True    


    
        