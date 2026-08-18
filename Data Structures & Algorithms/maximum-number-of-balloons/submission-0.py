from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequencies of characters in the text
        text_count = Counter(text)
        
        # We only care about letters in "balloon"
        # 'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1
        return min(
            text_count['b'],
            text_count['a'],
            text_count['l'] // 2,
            text_count['o'] // 2,
            text_count['n']
        )
