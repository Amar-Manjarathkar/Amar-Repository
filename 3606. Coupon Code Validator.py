class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Define the required order of business lines
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        
        valid_coupons = []
        
        for i in range(len(code)):
            c = code[i]
            bl = businessLine[i]
            active = isActive[i]
            
            # Check conditions:
            # 1. isActive[i] == true
            # 2. businessLine is one of the four valid categories
            # 3. code is non-empty and contains only alphanumeric + underscore
            if (active and
                bl in order and
                c and  # non-empty
                all(ch.isalnum() or ch == '_' for ch in c)):
                
                valid_coupons.append((bl, c))
        
        # Sort by:
        # 1. businessLine in specified order (using order dict)
        # 2. code lexicographically
        valid_coupons.sort(key=lambda x: (order[x[0]], x[1]))
        
        # Return only the codes
        return [coupon[1] for coupon in valid_coupons]
