//Euclid’s algorithm for finding the greatest common divisor of two numbers

public class gcd{
	//recursive implementation
	public static int gcd(int p, int q){
		if (q == 0) return p;
		return gcd(q, p % q);
	}

	//non-recursive implementation
	public static void gcd2 (int p, int q){
		while (q != 0){
			int temp = q;
			q = p % q;
			p = temp;
		}
		return p;
	}

	public static void main(String[] args){
		System.out.println(gcd(16, 20));
	}
}