/*
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true
 

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
*/

class Solution {
    public boolean isStrobogrammatic(String num) {
        Map<Character, Character> mirrors = new HashMap<> (
            Map.of('0', '0', '1', '1', '6', '9', '8', '8', '9', '6')
        );
        
        int left = 0, right = num.length() - 1;
        while (left <= right) {
            char leftChar = num.charAt(left);
            char rightChar = num.charAt(right);
            if (!mirrors.containsKey(leftChar) || mirrors.get(leftChar) != rightChar)
                return false;
            left++;
            right--;
        }
        
        return true;
    }
}

