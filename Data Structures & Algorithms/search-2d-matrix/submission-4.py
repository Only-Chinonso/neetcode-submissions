class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row,col = len(matrix),len(matrix[0])
        top,bot = 0,row - 1
        while top <= bot:
            m = (bot + top) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        l,r = 0,col - 1
        while l <= r:
            mid = (r + l) // 2
            if target > matrix[m][mid]:
                l = mid + 1
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                return True
        return False