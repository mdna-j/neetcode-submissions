class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        mapping = {}
        used_words = set()
        
        for c, w in zip(pattern, words):
            if c not in mapping:
                if w in used_words:
                    return False
                mapping[c] = w
                used_words.add(w)
            elif mapping[c] != w:
                return False
        
        return True