package day1;

public class Prime {

	public void isPrime(int num2) {
		if (num2 <= 1) {
			System.out.println("It is not a prime number");
			return;
		}

		if (num2 == 2) {
			System.out.println("It is a prime number");
			return;
		}

		boolean isPrime = true;

		// Check divisibility up to sqrt(num2)
		for (int i = 2; i <= Math.sqrt(num2); i++) {
			if (num2 % i == 0) {
				isPrime = false;
				break; // break only if divisible
			}
		}

		if (isPrime) {
			System.out.println("It is a prime number");
		} else {
			System.out.println("It is not a prime number");
		}
	}
}
