class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            # Add 0 at the beginning and end of the last row
            temp = [0] + res[-1] + [0]
            row = []
            # Sum adjacent elements to form the new row
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
            
        return res
