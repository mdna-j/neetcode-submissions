class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            val=list(i)
            val.sort()
            value=''.join(val)
            if value in d:
                d[value].append(i)
            else:
                d[value]=[i]
            
        return list(d.values())