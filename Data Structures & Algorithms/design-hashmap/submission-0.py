class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Choose a prime number or fixed capacity for buckets to distribute keys well
        self.num_buckets = 1000
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _get_bucket_index(self, key: int) -> int:
        """
        Helper method to get the bucket index using a simple modulo hash.
        """
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self._get_bucket_index(key)
        bucket = self.buckets[idx]
        
        # Check if key already exists, if so update its value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # If key does not exist, append the new pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key.
        """
        idx = self._get_bucket_index(key)
        bucket = self.buckets[idx]
        
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if 
        this map contains a mapping for the key.
        """
        idx = self._get_bucket_index(key)
        bucket = self.buckets[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)