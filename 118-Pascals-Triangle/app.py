class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        current_row = 0
        result = []
        # For first list
        if len(result) == 0 and numRows != 0:
            result.append([1])
            numRows -= 1
            current_row += 1

        if numRows != 0:
            # Create List for each of Rows
            while numRows > 0:
                # First Add 1 to first and last of list
                current_row += 1
                result.append([1,1])
                if len(result[-1]) != current_row:
                    # Loop on current row without 1 (first and last)
                    result[-1][1:1] = [result[-2][j] + result[-2][j + 1] for j in range(len(result[-2])) if j != len(result[-2]) -1]
                numRows -= 1

        return result
            