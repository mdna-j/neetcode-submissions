class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Step 1: Count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Group numbers into buckets by frequency
        for n, c in count.items():
            freq[c].append(n)
        
        # Step 3: Collect the top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res