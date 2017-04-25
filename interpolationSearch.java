import java.util.*;

public class interpolationSearch {
	public static void main(String[] args){
		int[] array = new int[]{1, 4, 5, 7, 8, 9, 12, 14, 15, 17, 20, 24,
								26, 34, 36, 37, 46, 47, 48, 50, 61, 63, 65};
		Scanner scan = new Scanner(System.in);
		System.out.print("Please enter a number you want to search: ");
		int input = scan.nextInt();

		int hi = array.length - 1;
		int lo = 0;
		int index = -1;
		while (lo <= hi && input >= array[lo] && input <= array[hi]){
			int pos = lo + (int)((input - array[lo]) * (hi - lo) / (array[hi] - array[lo]));

			if (array[pos] == input){
				index = pos;
				break;
			}	
			if (array[pos] < input) lo = pos + 1;
			else hi = pos - 1;
		}
		System.out.println("The index of the number is: " + index);
	}
}



/*
The Interpolation Search is an improvement over Binary Search for instances,
where the values in a sorted array are uniformly distributed.
Binary Search always goes to middle element to check.
On the other hand interpolation search may go to different locations according the value of key being searched.
For example if the value of key is closer to the last element,
interpolation search is likely to start search toward the end side.
*/