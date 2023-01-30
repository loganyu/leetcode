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

class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int ai = a.length() - 1, bi = b.length() - 1, carry = 0;
        while (ai >= 0 || bi >= 0 || carry > 0) {
            if (ai >= 0 && a.charAt(ai) == '1')
                carry += 1;
            if (bi >= 0 && b.charAt(bi) == '1')
                carry += 1;
            
            if (carry % 2 == 1)
                sb.append('1');
            else
                sb.append('0');
            
            carry /= 2;
            ai--;
            bi--;
        }
        
        return sb.reverse().toString();
    }
}

