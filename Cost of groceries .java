import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt(); // total items 
            int x = scanner.nextInt(); // min freshness
            int[] a = new int[n]; // freshness arrays 
            int[] b = new int[n]; // cost array

            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt(); // fill the damn freshness array
            }

            for (int j = 0; j < n; j++) {
                b[j] = scanner.nextInt(); // fill the damn cost array
            }

            // Your code goes here
            int total_cost = 0;
            for (int i = 0; i < n; i++) {
                if (a[i] >= x) { // codition to check the freshness
                    total_cost += b[i]; // total cost calculation if above  condition is met
                }
            }
            System.out.println(total_cost);

        }
    }
}
