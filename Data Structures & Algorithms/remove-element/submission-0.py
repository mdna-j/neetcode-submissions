class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Index to track where the next non-val element should go
        k = 0 
        
        # Iterate through all elements in the array
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Move it to the front at position k
                nums[k] = nums[i]
                # Increment the write pointer
                k += 1
                
        # k represents the count of elements not equal to val
        return k