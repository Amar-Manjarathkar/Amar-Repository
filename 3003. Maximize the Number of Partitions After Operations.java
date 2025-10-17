import java.util.HashMap;
import java.util.Map;

class Solution {
    private int n;
    private String s;
    private int k;
    private Map<Integer, Integer>[][] memo;

    public int maxPartitionsAfterOperations(String s, int k) {
        this.n = s.length();
        this.s = s;
        this.k = k;
        
        // Initialize memoization table
        // memo[index][canChange] stores a map from mask to result
        this.memo = new HashMap[n + 1][2];
        for (int i = 0; i <= n; i++) {
            memo[i][0] = new HashMap<>();
            memo[i][1] = new HashMap<>();
        }
        
        // The initial call starts at index 0, with an empty mask (0), 
        // and the ability to change a character (canChange = 1).
        return solve(0, 0, 1);
    }

    private int solve(int index, int currentMask, int canChange) {
        // Base case: If we have processed the entire string, we're done.
        // This counts as the final partition.
        if (index == n) {
            return 1;
        }

        // Check memoization table
        if (memo[index][canChange].containsKey(currentMask)) {
            return memo[index][canChange].get(currentMask);
        }

        int result;

        // --- Case 1: Don't change the character at s[index] ---
        int charBit = 1 << (s.charAt(index) - 'a');
        int nextMask = currentMask | charBit;
        
        if (Integer.bitCount(nextMask) > k) {
            // Must start a new partition. This adds 1 to the count.
            // The new partition starts with just s[index].
            result = 1 + solve(index + 1, charBit, canChange);
        } else {
            // Continue the current partition.
            result = solve(index + 1, nextMask, canChange);
        }

        // --- Case 2: Change the character at s[index] (if allowed) ---
        if (canChange == 1) {
            // Try changing s[index] to every possible character 'a' through 'z'.
            for (char ch = 'a'; ch <= 'z'; ch++) {
                int newCharBit = 1 << (ch - 'a');
                int changedNextMask = currentMask | newCharBit;
                
                int currentChangeResult;
                if (Integer.bitCount(changedNextMask) > k) {
                    // Start a new partition. Change has been used.
                    currentChangeResult = 1 + solve(index + 1, newCharBit, 0);
                } else {
                    // Continue the current partition. Change has been used.
                    currentChangeResult = solve(index + 1, changedNextMask, 0);
                }
                // Keep the maximum result.
                result = Math.max(result, currentChangeResult);
            }
        }
        
        // Store result in memoization table and return it.
        memo[index][canChange].put(currentMask, result);
        return result;
    }
}
