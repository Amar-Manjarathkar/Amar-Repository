class Solution {
    public int countBuildings(int[] height) {
        if (height == null || height.length == 0) {
            return 0;
        }

        int count = 0;
        int maxHeightSoFar = 0;

        for (int currentHeight : height) {
            if (currentHeight > maxHeightSoFar) {
                count++;
                maxHeightSoFar = currentHeight;
            }
        }
        
        return count;
    }
}
