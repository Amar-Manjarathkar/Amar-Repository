import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);// scanner class initislization
		
		int T = sc.nextInt();
		while(T-- > 0) // how many testcases ?
		{
		    int N =sc.nextInt(); // length of an array
		    int[] heights = new int[N]; // initialization of heights array
		    for (int i =0; i<N; i++)
		    {
		        heights[i] = sc.nextInt();// appending the arrays 
		    }
		    System.out.println(Arrays.stream(heights).max().getAsInt());//Stream. max() returns the maximum element of the stream based on the provided Comparator
		}
		sc.close();
		 
		

	}
}
