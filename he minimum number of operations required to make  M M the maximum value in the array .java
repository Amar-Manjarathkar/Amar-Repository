import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt(); // size of an array
            int[] a = new int[n]; // actual array

            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }

            // Your code goes here
            // to find the minimum element in the array
            int min = a[0];
            for (int i = 0; i < n; i++) {
                if (a[i] < min) {
                    min = a[i];
                }
            }

            int count = 0;
            for (int i = 0; i < n; i++) {
                if (a[i] == min) {
                    count++;
                }
            }
            System.out.println(n - count);
        }
    }
}
