class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = []
        row = [1]
        for i in range(numRows):
            if i > 0:
                x = []
                j = 0
                while j < len(new_row) - 1:
                    t = new_row[j] + new_row[j + 1]
                    x.append(t)
                    j += 1
                row = x
            pascals.append(row)
            new_row = [0] + row + [0]
        return pascals