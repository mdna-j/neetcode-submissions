class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Build frequency map
        counts = Counter(arr)
        
        # Second pass to find kth distinct
        for string in arr:
            if counts[string] == 1:
                k -= 1
                if k == 0:
                    return string
                    
        return ""