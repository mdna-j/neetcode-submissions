class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        # sort the string in the array
        for s in strs:
            sorted_s = "".join(sorted(s))

            # place the sorted as index if not in hashmap
            if sorted_s not in hashmap:
                hashmap[sorted_s] = []

            # add in the string to the index
            hashmap[sorted_s].append(s)

        return list(hashmap.values())