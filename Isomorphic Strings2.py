class Solution:
    def areIsomorphic(self, s1, s2):
        
        map1 = {}
        map2 = {}
        
        for c1, c2 in zip(s1, s2):
            
            # Check s1 -> s2 mapping
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2
            
            # Check s2 -> s1 mapping
            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1
                
        return True
