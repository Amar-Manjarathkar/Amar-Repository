class Solution:
    def minDist(self, arr, x, y):
        n = len(arr)
        last_x = -1
        last_y = -1
        min_dist = float('inf')

        for i in range(n):
            if arr[i] == x:
                last_x = i
                if last_y != -1:
                    min_dist = min(min_dist, abs(last_x - last_y))
            
            if arr[i] == y:
                last_y = i
                if last_x != -1:
                    min_dist = min(min_dist, abs(last_x - last_y))

        return min_dist if min_dist != float('inf') else -1
