class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        count = {}
    
        # Count frequencies
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Decrement frequencies
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                del count[char]
            
        # If the map is empty, all characters matched
        return len(count) == 0