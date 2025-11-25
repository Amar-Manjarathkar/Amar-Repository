class Solution:
    """
    Computes the bitwise XOR of the values of all possible subarrays of arr[].
    The value of a subarray is the bitwise XOR of all its elements.
    """
    def subarrayXor(self, arr):
        n = len(arr)
        final_xor = 0
        
        # An element arr[i] contributes to the final XOR sum 
        # only if the total number of subarrays it belongs to, 
        # (i + 1) * (n - i), is ODD.
        # This occurs if and only if (i + 1) is ODD AND (n - i) is ODD.
        # 1. (i + 1) is ODD -> i is EVEN
        # 2. (n - i) is ODD -> n and i have different parity
        
        # Combining these: i must be EVEN, and n must be ODD.
        # If n is even, no element contributes (final_xor is 0).
        
        for i in range(n):
            # Check if (i+1) * (n-i) is odd
            # This is equivalent to checking if both factors are odd:
            # (i + 1) % 2 == 1 AND (n - i) % 2 == 1
            
            is_start_count_odd = (i + 1) % 2 == 1 # Equivalent to i being even
            is_end_count_odd = (n - i) % 2 == 1   # Equivalent to n and i having different parity
            
            if is_start_count_odd and is_end_count_odd:
                final_xor ^= arr[i]
                
        return final_xor

# Example usage:
# arr = [1, 2, 3] -> n=3 (odd). Indices 0, 2 are even.
# Elements: arr[0]=1, arr[2]=3 contribute. Final XOR = 1 ^ 3 = 2.
# arr = [1, 2, 3, 4] -> n=4 (even). No element contributes. Final XOR = 0.
