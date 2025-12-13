class Solution:
    def swapDiagonal(self, mat):
      # code here
      n=len(mat)
      for i in range(n):
          for j in range(n):
              if i == j:
                mat[i][i], mat[i][n-1-i] = mat[i][n-1-i], mat[i][i]
      return mat
