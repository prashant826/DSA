#https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Returning ouput for input 1 and 2
        if numRows == 1:
            return [[1]]   
        if numRows == 2:
            return [[1],[1,1]]

        # To Calculate current Row, Starting and ending element of every row will be 1.
        output = [[1] , [1,1]]
        for i in range(3,numRows+1):
            currRowLength = i
            newRow = [1]*currRowLength # Current Row length will be current iterator (ith).
            for j in range(1, len(output[-1])):
                # Starting from index 1 for newRow our value will be addition of the consecutive element from previous row.
                newRow[j] = output[-1][j] + output[-1][j-1]
            output.append(newRow)
        return output