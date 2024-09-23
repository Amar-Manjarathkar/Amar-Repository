import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), X = sc.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) A[i] = sc.nextInt();

        // Use Arrays.stream for a shorter search
        System.out.println(Arrays.stream(A).anyMatch(n -> n == X) ? "YES" : "NO");
		

	}
}
