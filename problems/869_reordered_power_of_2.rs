/*
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
*/

impl Solution {
    fn count_digits(mut n: i32) -> [i8; 10] {
        let mut counts = [0; 10];
        while n > 0 {
            counts[(n % 10) as usize] += 1;
            n /= 10;
        }
        counts
    }

    pub fn reordered_power_of2(n: i32) -> bool {
        let n_counts = Self::count_digits(n);

        for i in 0..30 {
            let power_of_2 = 1 << i;

            if Self::count_digits(power_of_2) == n_counts {
                return true;
            }
        }

        false
    }
}

