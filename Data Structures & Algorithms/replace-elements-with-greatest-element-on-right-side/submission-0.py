class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
    
    # Iterate from the last index to the first index
        for i in range(len(arr) - 1, -1, -1):
            current_val = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, current_val)
        
        return arr