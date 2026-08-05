class MyHashSet {
private:
    int num_buckets;
    std::vector<std::list<int>> buckets;

    // Hash function to map key to a bucket index
    int hash(int key) {
        return key % num_buckets;
    }

public:
    // Initialize data structure with a prime number of buckets to reduce collisions
    MyHashSet() {
        num_buckets = 13013; 
        buckets.resize(num_buckets);
    }
    
    // Insert a value into the HashSet
    void add(int key) {
        int index = hash(key);
        auto& bucket = buckets[index];
        
        // Only add if the key does not already exist
        if (std::find(bucket.begin(), bucket.end(), key) == bucket.end()) {
            bucket.push_back(key);
        }
    }
    
    // Remove a value from the HashSet
    void remove(int key) {
        int index = hash(key);
        auto& bucket = buckets[index];
        auto it = std::find(bucket.begin(), bucket.end(), key);
        
        // If found, remove it from the list
        if (it != bucket.end()) {
            bucket.erase(it);
        }
    }
    
    // Return true if the value exists in the HashSet
    bool contains(int key) {
        int index = hash(key);
        const auto& bucket = buckets[index];
        return std::find(bucket.begin(), bucket.end(), key) != bucket.end();
    }
};


/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */