class Solution {
    int thirdLargest(int arr[]) {
        // Your code here
        int res = -1;
        int n = arr.length;
        Arrays.sort(arr);
        res= arr[n-3];
        return res;
    }
}
