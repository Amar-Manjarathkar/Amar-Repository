class Solution:
    def josephus(self, n, k):
        # Base case: If only one person remains, they are at index 0 (0-based)
        if n == 1:
            return 1 # Returning 1 directly for 1-based logic
        
        # Recursive step: (Recursive Result + k - 1) % n + 1
        # We use (f(n-1, k) + k - 1) % n + 1 to keep it in 1-based indexing
        return (self.josephus(n - 1, k) + k - 1) % n + 1
