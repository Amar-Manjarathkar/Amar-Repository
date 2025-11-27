class Solution:
    def subsetXORSum(self, arr: list[int]) -> int:
        n = len(arr)
        
        # 1. Calculate the Bitwise OR of all elements in the array
        bitwise_or_of_all = 0
        for x in arr:
            bitwise_or_of_all |= x
            
        # 2. Calculate the factor 2^(n-1)
        # (1 << (n - 1)) is the efficient way to calculate 2^(n-1)
        power_of_2_factor = 1 << (n - 1)
        
        # 3. Apply the formula: 2^(n-1) * (Bitwise OR)
        return power_of_2_factor * bitwise_or_of_all
