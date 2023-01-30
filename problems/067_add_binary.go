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

func addBinary(a string, b string) string {
    sum := 0
    carry := 0
    res := ""
    ai := len(a) - 1
    bi := len(b) - 1
    
    for ai >= 0 || bi >= 0 || carry > 0 {
        sum = carry
        if ai >= 0 {
            sum += int(a[ai] - '0')
            ai--
        }
        if bi >= 0 {
            sum += int(b[bi] - '0')
            bi--
        }
        carry = sum / 2
        res = string(sum % 2 + '0') + res
    }
    
    return res
}

