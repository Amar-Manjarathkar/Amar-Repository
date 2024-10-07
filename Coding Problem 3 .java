import java.util.Scanner;

class Codechef
{
    public static void main(String[] args)
    {
        // your code goes here
        Scanner read = new Scanner(System.in);
        int N = read.nextInt();
        int X = read.nextInt();
        int[] arr1 = new int[N];
        int[] arr2 = new int[X];

        for (int i = 0; i < N; i++) {
            arr1[i] = read.nextInt();
        }

        for (int i = 0; i < X; i++) {
            arr2[i] = read.nextInt();
        }

        for (int i = 0; i < N; i++) {
            System.out.print(arr1[i] + " ");

        }
        for (int i = 0; i < X; i++) {
            System.out.print(arr2[i] + " ");

        }
        for (int i = 0; i < N; i++) {
            System.out.print(arr1[i] + " ");

        }

    }
}
