import java.util.Arrays;

class Solution {

    int maxValue(int arr[]) {
        Arrays.sort(arr);
        int n = arr.length;
        long MOD = 1000000007;
        long res = 0;
        
        for (int i = 0; i < n; i++) {
            res = (res + (long) arr[i] * i) % MOD;
        }
        
        return (int) res;
    }
}
