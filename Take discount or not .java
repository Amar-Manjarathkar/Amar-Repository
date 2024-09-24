import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt(); // total items
            int x = scanner.nextInt(); // Coupon price
            int y = scanner.nextInt(); // Discount Price
            int[] a = new int[n];
            int sum = 0; // to  store sum of arrays elements
            int Discount = 0; // to store the Discount applied

            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
                sum += a[i]; // toal cost of the item
                if (a[i] >= y) {
                    Discount += a[i] - y; // Discount applied
                }
            }

            if (sum > Discount + x)
            {
                System.out.println("Coupon");
            }
            else {
                System.out.println("No Coupon");
            }
        }
    }
}
