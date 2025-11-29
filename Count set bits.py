class Solution:
    def countSetBits(self, n):
        if n < 0:
            return 0
        count = 0
        i = 1
        while i <= n:
            divisor = i << 1  # 2 * i
            full = (n + 1) // divisor
            count += full * i
            
            extra = (n + 1) % divisor
            if extra > i:
                count += extra - i
            
            i = divisor  # i <<= 1
        return count
        
