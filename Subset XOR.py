class Solution:
    def subsetXOR(self, n: int):
        mod = n % 4
        if mod == 0:
            xor_all = n
        elif mod == 1:
            xor_all = 1
        elif mod == 2:
            xor_all = n + 1
        else:
            xor_all = 0
        target = xor_all ^ n
        if target == 0:
            return list(range(1, n + 1))
        else:
            return [i for i in range(1, n + 1) if i != target]
