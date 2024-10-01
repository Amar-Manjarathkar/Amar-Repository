import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); // Read the number of test cases

        while (t-- > 0) {
            int n = scanner.nextInt(); // Read the size of the array
            int[] a = new int[n]; // Initialize the array

            // Reading the array elements
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }

            // Edge case: If there are fewer than 2 elements, skip processing
            if (n < 2) {
                System.out.println("Array must contain at least two elements");
                continue;
            }

            // Your code to find the maximum sum of two distinct integers
            int max1 = Integer.MIN_VALUE; // To store the largest element
            int max2 = Integer.MIN_VALUE; // To store the second largest element

            // Traverse the array to find the two largest distinct elements
            for (int i = 0; i < n; i++) {
                if (a[i] > max1) {
                    max2 = max1;
                    max1 = a[i];
                } else if (a[i] > max2 && a[i] != max1) {
                    max2 = a[i];
                }
            }

            // Output the sum of the two largest distinct numbers
            System.out.println(max1 + max2);
        }

        scanner.close(); // Close the scanner resource
    }
}
