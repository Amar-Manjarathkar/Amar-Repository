class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        mapping_s1 = {}
        mapping_s2 = {}
        
        for c1, c2 in zip(s1, s2):
            # Check mapping from s1 to s2
            if c1 in mapping_s1:
                if mapping_s1[c1] != c2:
                    return False
            else:
                mapping_s1[c1] = c2
            
            # Check mapping from s2 to s1 (to ensure one-to-one)
            if c2 in mapping_s2:
                if mapping_s2[c2] != c1:
                    return False
            else:
                mapping_s2[c2] = c1
        
        return True
