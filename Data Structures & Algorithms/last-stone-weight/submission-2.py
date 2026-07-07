class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        while True:
            l=[]
            stones.sort(reverse = True)
            y = stones.pop(0)
            x = stones.pop(0)
            if y==x:
                l.extend(stones)
                if len(stones)==0:
                    l.append(0)
            else:
                l.append(abs(x-y))
                l.extend(stones)
            stones = l
            print(x,y,l)
            if len(l)==1:
                return l[0]
            
            