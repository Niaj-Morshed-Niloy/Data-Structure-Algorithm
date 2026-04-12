"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rowtrack=[0 for _ in range(r)]
        coltrack=[0 for _ in range(c)]
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    coltrack[j]=-1
        for i in range(0,r):
            for j in range(0,c):
                if rowtrack [i]==-1 or coltrack[j]==-1:
                    matrix[i][j]=0
