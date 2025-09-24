import java.util.Arrays;

class Solution {
    public void mergeArrays(int a[], int b[]) {
        int n = a.length, m = b.length;
        int i = n - 1, j = 0;

        // Step 1: Swap out-of-order elements
        while (i >= 0 && j < m) {
            if (a[i] > b[j]) {
                int temp = a[i];
                a[i] = b[j];
                b[j] = temp;
            }
            i--;
            j++;
        }

        // Step 2: Sort both arrays
        Arrays.sort(a);
        Arrays.sort(b);
    }
}

