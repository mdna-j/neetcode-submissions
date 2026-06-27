class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer forward if it's not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer backward if it's not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare the characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
                
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True

        