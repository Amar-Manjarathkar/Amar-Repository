import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt(); // Read the number of elements

        int[] arr = new int[N + 2]; // Create an array with size N + 2

        // Read the N space separated integers and store them in the array
        for (int i = 1; i <= N; i++) {
            arr[i] = scanner.nextInt();
        }
        int X = scanner.nextInt(); // Read the integer X
        // Insert X as the first element
        arr[0] = X;

        // Insert X as the last element
        arr[N + 1] = X;

        // Output the updated list
        for (int i = 0; i < N + 2; i++) {
            System.out.print(arr[i] + " ");
        }

	}
}
