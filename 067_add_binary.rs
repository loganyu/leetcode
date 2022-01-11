/*
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
*/

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut res: Vec<char> = vec![];
        let v_a: Vec<char> = a.chars().collect();
        let v_b: Vec<char> = b.chars().collect();
        
        let mut carry = 0;
        let mut ai = a.len();
        let mut bi = b.len();
        
        while ai > 0 || bi > 0 || carry > 0 {
            if ai > 0 {
                ai -= 1;
                carry += v_a[ai] as u8 - 48;
            }
            if bi > 0 {
                bi -= 1;
                carry += v_b[bi] as u8 - 48;
            }
            res.push((carry % 2 + 48) as char);
            carry /= 2;
        }
        
        res.iter().rev().collect::<String>()
    }
}

