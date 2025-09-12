import java.util.Pair; // You might need to import or define a Pair class

class Solution {
    public Pair<Integer, Integer> getMinMax(int[] arr) {
        // Handle the edge case of an empty or null array
        if (arr == null || arr.length == 0) {
            // Or throw an exception, depending on requirements
            return null;
        }

        // 1. Initialize min and max with the first element
        int min = arr[0];
        int max = arr[0];

        // 2. Iterate from the second element to the end of the array
        for (int i = 1; i < arr.length; i++) {
            // 3. If the current element is smaller than min, update min
            if (arr[i] < min) {
                min = arr[i];
            }
            // 4. If the current element is larger than max, update max
            else if (arr[i] > max) {
                max = arr[i];
            }
        }

        // 5. Return the result as a new Pair object
        return new Pair<>(min, max);
    }
}
