package day1;

public class Fibonacci {
	int num;
	
	public static void fib(int num) {
		int a = 0;
		int b = 1;
		int temp;
		if (num<0) System.out.println("Enter a non-negative number");
		if (num==0) System.out.println("0");
		if (num==1) System.out.println("0,1");
		System.out.println("The Fibonacci series for "+num+" digit is:");
		System.out.print(a+",");
		for(int i=2; i<=num;i++) {
			temp=a+b;
			System.out.print(temp+",");
			a=b;
			b=temp;
		}
		
		System.out.println();
	
	}
	
}
