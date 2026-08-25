class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        
        # Count each character in the magazine
        for c in magazine:
            count[ord(c) - ord('a')] += 1
            
        # Subtract counts using the ransom note
        for c in ransomNote:
            index = ord(c) - ord('a')
            count[index] -= 1
            if count[index] < 0:
                return False
                
        return True