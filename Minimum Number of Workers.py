class Solution:
    def minMen(self, arr):
        n = len(arr)

        if n == 1:
            return 1 if arr[0] != -1 else -1

        # Preprocessing
        max_reach = [-1] * n
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                max_reach[left] = max(max_reach[left], right)

        # Greedy coverage
        workers = 0
        current_end = -1
        next_end = -1

        for i in range(n):
            next_end = max(next_end, max_reach[i])

            if i > current_end:
                # ❗ FIX: If this position is unreachable
                if next_end < i:
                    return -1

                workers += 1
                current_end = next_end

                if current_end >= n - 1:
                    return workers

        return -1
