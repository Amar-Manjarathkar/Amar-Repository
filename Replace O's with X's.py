class Solution:
    def fill(self, grid):
        # Code here
        
        # Check for empty grid
        if not grid or not grid[0]:
            return grid

        n = len(grid)    # Number of rows
        m = len(grid[0]) # Number of columns

        # 1. Define the Depth First Search (DFS) helper function
        # This function will find all 'O's connected to a starting 'O'
        # and mark them as 'S' (Safe)
        def dfs(r, c):
            # Base cases for stopping the recursion:
            # 1. Out of bounds (row or column)
            # 2. Current cell is not an 'O' (it's 'X' or already visited 'S')
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != 'O':
                return
            
            # Mark the current 'O' as 'S' (Safe) to mark it as visited
            # and indicate it's connected to the border
            grid[r][c] = 'S'
            
            # Explore all 4 neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # 2. Mark all 'O's connected to the border as 'S' (Safe)
        
        # Iterate over the first and last row (top and bottom border)
        for j in range(m):
            # Top row
            if grid[0][j] == 'O':
                dfs(0, j)
            # Bottom row
            if grid[n - 1][j] == 'O':
                dfs(n - 1, j)
        
        # Iterate over the first and last column (left and right border)
        for i in range(n):
            # Left column
            if grid[i][0] == 'O':
                dfs(i, 0)
            # Right column
            if grid[i][m - 1] == 'O':
                dfs(i, m - 1)
        
        # 3. Iterate through the entire grid and flip the cells
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    # This 'O' is not connected to any border, so it's surrounded.
                    grid[i][j] = 'X'
                elif grid[i][j] == 'S':
                    # This 'O' was safe (connected to the border),
                    # so restore it back to 'O'.
                    grid[i][j] = 'O'
        
        return grid
