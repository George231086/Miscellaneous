/**
 * 
 * @author george
 * 
 *         Program to find the biggest palindrome
 *         that can factored into the product of two 3 digit numbers.
 */

public class bigPalindrome {

	public static void main(String args[]) {

		String pal;
		boolean isPal = true;

		outer: for (int i = 999 * 999; i > 100 * 100; i--) {
			isPal = true;
			pal = "" + i;
			// Check if palindrome.
			for (int j = 0; j < pal.length(); j++) {
				if (pal.charAt(j) != pal.charAt(pal.length() - j - 1))
					isPal = false;

			}
			// If a palindrome, check whether it can be factored into two 3
			// digit numbers.
			if (isPal) {
				for (int k = 999; k > 99; k--) {
					if (i % k == 0) {
						if (i / k > 99 && i / k < 1000) {
							System.out.println("Found it: " + i);
							// break out of all loops. Used label outer to mark
							// the main loop.
							break outer;
						}
					}

				}

			}
		}

	}

}
