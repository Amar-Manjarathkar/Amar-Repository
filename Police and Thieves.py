class Solution:
    def catchThieves(self, arr, k):
        n = len(arr)
        # 1. Use list comprehension to get all indices of P and T
        police = [i for i, x in enumerate(arr) if x == 'P']
        thieves = [i for i, x in enumerate(arr) if x == 'T']
        
        p = 0  # Pointer for police indices
        t = 0  # Pointer for thief indices
        caught = 0
        
        # 2. Match them greedily
        while p < len(police) and t < len(thieves):
            # If the current thief is within reach of the current policeman
            if abs(police[p] - thieves[t]) <= k:
                caught += 1
                p += 1
                t += 1
            # If the thief is too far behind the policeman, move to the next thief
            elif thieves[t] < police[p]:
                t += 1
            # If the policeman is too far behind the thief, move to the next policeman
            else:
                p += 1
                
        return caught
