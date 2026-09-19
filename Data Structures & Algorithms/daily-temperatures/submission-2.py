class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0 for _ in range(len(temperatures))]
        hottest = temperatures[len(temperatures) - 1]

        for idx in range(len(temperatures) - 2, -1, -1):
            temp = temperatures[idx]

            if temp >= hottest:
                hottest = temp
                continue

            j = idx + 1

            while temperatures[j] <= temp:
                j += ret[j]

            ret[idx] = j - idx
            
        return ret
