import java.util.*;

public class JumpSearch {
	public static void main(String[ ] args){
		int[] array = new int[]{1, 3, 5, 7, 8, 9, 23, 34, 56, 67, 68, 69, 90};
		Scanner scan = new Scanner(System.in);
		System.out.print("Please enter a number you want to search: ");
		int input = scan.nextInt();

		int m = (int)Math.sqrt(array.length);
		int index = -1;
		for (int i = 0; i < array.length; i += m) {
			if (array[i] == input) index = i;
			if (array[i] > input) {
				for (int j = i - m + 1; j < m; j++){
					if (array[j] == input) index = j;
				}
			}
		} 
		System.out.println("The index of the number you are searching for is: " + index);
	}
}





/*
We have an array arr[] of size n and block (to be jumped) size m.
Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on.
Once we find the interval (arr[km] < x < arr[(k+1)m]), 
we perform a linear search operation from the index km to find the element x.
*/