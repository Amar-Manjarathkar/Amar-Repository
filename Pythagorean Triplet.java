import java.util.HashSet;

class Solution {
    boolean pythagoreanTriplet(int[] arr) {
        int n = arr.length;
        long[] squared = new long[n];

        // Step 1: Square all elements
        for (int i = 0; i < n; i++) {
            squared[i] = 1L * arr[i] * arr[i];
        }

        // Step 2: Store all squares in a HashSet for O(1) lookup
        HashSet<Long> set = new HashSet<>();
        for (long val : squared) {
            set.add(val);
        }

        // Step 3: Check pairs (a², b²) and see if their sum exists in set
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long sum = squared[i] + squared[j];
                if (set.contains(sum)) {
                    return true;
                }
            }
        }

        return false;
    }
}
