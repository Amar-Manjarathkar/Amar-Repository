import java.util.Arrays;

class Solution {
    public static boolean areAnagrams(String s1, String s2) {
        // If lengths differ, they cannot be anagrams
        if (s1.length() != s2.length()) {
            return false;
        }

        // Convert strings to char arrays
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();

        // Sort both arrays
        Arrays.sort(arr1);
        Arrays.sort(arr2);

        // Compare sorted arrays
        return Arrays.equals(arr1, arr2);
    }
}
