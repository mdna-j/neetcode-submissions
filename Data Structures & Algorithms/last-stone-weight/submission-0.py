class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python's heapq is a min-heap, so we multiply by -1 to simulate a max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop the two heaviest stones (they will be the smallest numbers in our negative heap)
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            # If there's a difference, push the remainder back into the heap
            if first != second:
                heapq.heappush(max_heap, -(first - second))
                
        # Return the last remaining stone weight, or 0 if the heap is empty
        return -max_heap[0] if max_heap else 0
        