// User function Template for Java
class Solution {
    void segregate0and1(int[] arr) {
        int left = 0, right = arr.length - 1;
        
        while (left < right) {
            // Move left pointer if element is already 0
            while (arr[left] == 0 && left < right) {
                left++;
            }
            // Move right pointer if element is already 1
            while (arr[right] == 1 && left < right) {
                right--;
            }
            // Swap arr[left] and arr[right]
            if (left < right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
    }
}
