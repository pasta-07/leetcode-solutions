class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = (row*col)-1
        while left<=right:
            mid = (left+right) //2
            r = mid//col
            c = mid%col
            matrix_value = matrix[r][c]
            if matrix_value == target:
                return True
            elif matrix_value>target:
                right = mid-1
            else:
                left = mid+1
        return False