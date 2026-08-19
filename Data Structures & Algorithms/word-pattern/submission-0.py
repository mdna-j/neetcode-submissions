class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string s by spaces to get an array of words
        words = s.split(" ")
        
        # If the lengths don't match, they cannot have a 1-to-1 mapping
        if len(pattern) != len(words):
            return False
        
        # Initialize hash maps for bidirectional mapping
        charToWord = {}
        wordToChar = {}
        
        # Iterate through both sequences simultaneously
        for c, w in zip(pattern, words):
            # Check character-to-word consistency
            if c in charToWord and charToWord[c] != w:
                return False
            
            # Check word-to-character consistency
            if w in wordToChar and wordToChar[w] != c:
                return False
            
            # Establish the mapping in both maps
            charToWord[c] = w
            wordToChar[w] = c
            
        return True

        