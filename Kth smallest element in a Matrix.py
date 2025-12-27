class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        
        # Helper function nested inside to access 'mat' and 'n' easily
        def countLessEqual(mid):
            count = 0
            row = n - 1  # Start from the bottom-left corner
            col = 0
            while row >= 0 and col < n:
                if mat[row][col] <= mid:
                    # All elements above this in the current column are also <= mid
                    count += (row + 1)
                    col += 1
                else:
                    row -= 1
            return count

        low = mat[0][0]
        high = mat[n-1][n-1]
        ans = low
        
        while low <= high:
            mid = low + (high - low) // 2
            # Use the nested helper function
            if countLessEqual(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
