import java.util.Scanner;

class Codechef
{
    public static void main(String[] args)
    {
        // your code goes here
        Scanner read = new Scanner(System.in);
        int N = read.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = read.nextInt();
        }
        int X = read.nextInt();
        int k = 0;
        // int[] updated = new int[N];

        for (int i = 0; i < N; i++) {
            if (arr[i] != X) {
                arr[k] = arr[i];
                k++;
            }
        }

        for (int i = 0; i < k; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}
