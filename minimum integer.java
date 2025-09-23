class Solution {
    public static int minimumInteger(int N, int[] A) {
        long S = 0;
        for (int val : A) {
            S += val;
        }

        int minX = Integer.MAX_VALUE;

        for (int X : A) {
            if (S <= (long)N * X) {
                minX = Math.min(minX, X);
            }
        }
        
        return minX;
    }
}
