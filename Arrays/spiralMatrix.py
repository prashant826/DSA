# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix) , len(matrix[0])
        output = []
        top, right, bottom, left = 0, col-1, row-1, 0
        while len(output) < row*col:
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top+=1
            for i in range(top, bottom+1):
                output.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right, left-1,-1):
                    output.append(matrix[bottom][i])
                bottom-=1
            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
        return output