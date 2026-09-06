class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        # turns the array into a min-heap in 0(n) time complexity
        heapq.heapify(self.minHeap) 

        # ensures the heap size doesn't exceed k 
        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)

        

    def add(self, val: int) -> int:
        # Pushes the new value and pops if it exceeds the size of k
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The top of the heap is the Kth largest element
        return self.minHeap[0]
    
        
