class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        
        def dfs(r, c, index):
            # Base case: All characters found
            if index == len(word):
                return True
            
            # Boundary checks and character matching
            if (r < 0 or r >= n or c < 0 or c >= m or 
                mat[r][c] != word[index]):
                return False
            
            # Mark as visited by saving and changing the value
            temp = mat[r][c]
            mat[r][c] = '#'
            
            # Explore 4 directions: Right, Left, Down, Up
            found = (dfs(r + 1, c, index + 1) or 
                     dfs(r - 1, c, index + 1) or 
                     dfs(r, c + 1, index + 1) or 
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: Restore the original value
            mat[r][c] = temp
            
            return found

        # Try starting from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
