/*
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
*/

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut results: Vec<i32> = Vec::new();
        for digit in 1..10 {
            let mut num = digit;
            let mut next = digit;
            while num <= high && next < 10 {
                if num >= low {
                    results.push(num);
                }
                next += 1;
                num = num * 10 + next;
            }
        }
        results.sort();
        
        results
    }
}

