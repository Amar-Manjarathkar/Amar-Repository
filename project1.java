package day1;

import java.util.Scanner;

public class project1 {

	public static void main(String[] args) {
		System.out.println("Hello World");
		// TODO Auto-generated method stub
		Base b = new Base();
		b.test();
		System.out.println("Enter a number:");
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		Prime p = new Prime();
		p.isPrime(num);
		sc.close();

	}

}
