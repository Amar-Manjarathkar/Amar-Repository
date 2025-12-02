import collections

class Solution:
    def maxScore(self, s: str, jumps: list[list[str]]) -> int:
        n = len(s)
        # Use a large negative number for unreachable states
        NEG_INF = -10**18
        
        # --- 1. Preprocessing: Jump Graph and Character Data ---
        
        jump_set = set((s1, s2) for s1, s2 in jumps)
        all_chars = set(s) | set(j[0] for j in jumps) | set(j[1] for j in jumps)
        char_to_ord = {c: ord(c) for c in all_chars}
        
        # Adjacency[c1] stores all c2 such that c1 -> c2 is a valid jump (for updates)
        Adjacency = collections.defaultdict(set)
        # InverseAdjacency[c2] stores all c1 such that c1 -> c2 is a valid jump (for queries)
        InverseAdjacency = collections.defaultdict(set)
        
        for c1 in all_chars:
            for c2 in all_chars:
                if (c1, c2) in jump_set or c1 == c2:
                    Adjacency[c1].add(c2)
                    InverseAdjacency[c2].add(c1)
        
        # --- 2. Preprocessing: Prefix Sums ---
        
        # P[i] = sum(ascii(s[0]) + ... + ascii(s[i-1]))
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + ord(s[i])
        
        # CountPrefix[c][i] = count of character c in s[0...i-1]
        CountPrefix = {c: [0] * (n + 1) for c in all_chars}
        for i in range(n):
            for c in all_chars:
                CountPrefix[c][i+1] = CountPrefix[c][i]
            # Update count for the current character s[i]
            if s[i] in CountPrefix:
                CountPrefix[s[i]][i+1] += 1
        
        # --- 3. Dynamic Programming Initialization ---
        
        # DP[i] = max score ending at index i
        DP = [NEG_INF] * n
        DP[0] = 0
        
        # Max_V[c1][c2] stores max(DP[i] - P[i] + CountPrefix[c2][i] * ascii(c2)) for s[i] = c1
        # This is the 'variable' part of the jump equation.
        Max_V = collections.defaultdict(lambda: collections.defaultdict(lambda: NEG_INF))
        
        max_total_score = 0
        
        # --- 4. DP Iteration (O(n * |J_total|)) ---
        for j in range(n):
            c2 = s[j]
            ord_c2 = char_to_ord.get(c2, 0)
            
            # A. Calculate DP[j] (find max incoming jump score)
            if j > 0 and c2 in InverseAdjacency:
                # The 'constant' part of the jump equation for a jump to index j
                # constant = P[j] - CountPrefix[c2][j] * ord_c2
                const_term = P[j] - CountPrefix[c2][j] * ord_c2
                
                # Iterate ONLY over valid origin characters c1
                for c1 in InverseAdjacency[c2]:
                    max_v_i = Max_V[c1][c2]
                    if max_v_i > NEG_INF:
                        # DP[j] = max_v_i + const_term
                        DP[j] = max(DP[j], max_v_i + const_term)
            
            # --- Update Phase ---
            if DP[j] > NEG_INF:
                # Update the global max score
                max_total_score = max(max_total_score, DP[j])
                
                # B. Update Max_V (prepare for future jumps starting at j)
                c1 = s[j]
                
                # Iterate ONLY over valid destinations c_new from c1
                for c_new in Adjacency[c1]:
                    ord_c_new = char_to_ord.get(c_new, 0)
                    
                    # V_new = DP[j] - P[j] + CountPrefix[c_new][j] * ascii(c_new)
                    # Note: We use P[j] and CountPrefix up to s[j-1] (index j).
                    V_new = DP[j] - P[j] + CountPrefix[c_new][j] * ord_c_new
                    
                    Max_V[c1][c_new] = max(Max_V[c1][c_new], V_new)

        return max_total_score
