class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        low = 0
        high = cols - 1
        
        while low <= high:
            mid_col = (low + high) // 2
            
            # 1. Find the row index of the maximum element in the middle column
            # We initialize max_row to 0 and compare from there
            max_row = 0
            for r in range(1, rows):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r
            
            # 2. Correctly handle boundaries using negative infinity
            curr_val = mat[max_row][mid_col]
            
            # If mid_col is 0, left neighbor is -infinity
            left_val = mat[max_row][mid_col - 1] if mid_col > 0 else float('-inf')
            
            # If mid_col is the last column, right neighbor is -infinity
            right_val = mat[max_row][mid_col + 1] if mid_col < cols - 1 else float('-inf')
            
            # 3. Check if the current element is a peak
            if curr_val >= left_val and curr_val >= right_val:
                return [max_row, mid_col]
            
            # 4. Move towards the larger neighbor
            elif left_val > curr_val:
                high = mid_col - 1
            else:
                low = mid_col + 1
                
        return []
