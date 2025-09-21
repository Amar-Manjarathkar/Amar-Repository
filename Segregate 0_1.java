// User function Template for Java
class Solution {
    void segregate0and1(int[] arr) {
        int count0 = 0;

        // Count number of 0s
        for (int num : arr) {
            if (num == 0) {
                count0++;
            }
        }

        // Fill first count0 elements with 0
        for (int i = 0; i < count0; i++) {
            arr[i] = 0;
        }

        // Fill remaining elements with 1
        for (int i = count0; i < arr.length; i++) {
            arr[i] = 1;
        }
    }
}
