class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        mapping = {}
        mapped = set()
        
        for c1, c2 in zip(s1, s2):
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            else:
                if c2 in mapped:  # prevents two chars from s1 mapping to same c2
                    return False
                mapping[c1] = c2
                mapped.add(c2)
        
        return True
