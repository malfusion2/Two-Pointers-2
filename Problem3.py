# Time Complexity : O(m+n) where m and n are the number of rows and columns
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# We start from a corner from where we can take decisions on which row or column 
# to exclude and proceed along the other dimension
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: 
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
                
        return False