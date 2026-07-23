class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        result = []

        for i, word in enumerate(words):
            if any(word in other for other in words [i + 1:]):
                result.append(word)

        return result     






