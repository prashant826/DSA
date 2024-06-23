# https://leetcode.com/problems/rotate-image/
# 00 01 02
# 10 11 12
# 20 21 22

# 00 10 20
# 01 11 12
# 20 21 22

# 20 10 00
# 21 11 01
# 22 12 02

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix) , len(matrix[0])
        # transpose
        for i in range(row):
            for j in range(i+1):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        #print(matrix)
        # reverse each row
        for i in range(row):
            matrix[i] = matrix[i][::-1]
        