import java.util.List;

class Solution {
    /**
     * Checks if a subarray of length k starting at index 'start' is strictly increasing.
     */
    private boolean isStrictlyIncreasing(List<Integer> nums, int start, int k) {
        if (k <= 1) {
            return true;
        }
        // Iterate from the second element up to the end of the k-length window
        for (int i = 1; i < k; i++) {
            // Check if the current element is strictly greater than the previous one
            if (nums.get(start + i) <= nums.get(start + i - 1)) {
                return false;
            }
        }
        return true;
    }

    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();

        // Edge Case: If the array is too short to contain two adjacent subarrays of length k
        if (n < 2 * k) {
            return false;
        }

        // The first subarray starts at 'a'. The second starts at 'a + k'.
        // The last possible starting index 'a' for the first subarray is when 'a + 2k - 1' 
        // equals 'n - 1', so a_max = n - 2k.
        for (int a = 0; a <= n - 2 * k; a++) {
            int b = a + k; // Start of the second, adjacent subarray

            // Check the first subarray: nums[a...a + k - 1]
            boolean firstIsIncreasing = isStrictlyIncreasing(nums, a, k);
            
            // Optimization: Only check the second subarray if the first one is valid
            if (firstIsIncreasing) {
                // Check the second subarray: nums[b...b + k - 1]
                boolean secondIsIncreasing = isStrictlyIncreasing(nums, b, k);

                if (secondIsIncreasing) {
                    return true;
                }
            }
        }

        return false;
    }
}
