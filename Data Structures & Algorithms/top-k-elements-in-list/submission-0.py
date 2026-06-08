class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies of each number
        count = Counter(nums)
        
        # Create buckets where index = frequency
        # Maximum possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Iterate backwards from highest frequency to find top k
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res