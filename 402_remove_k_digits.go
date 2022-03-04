/*
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
*/

func removeKdigits(num string, k int) string {
    stack := make([]byte, 0)
    for i := range num {
		for k > 0 && len(stack) > 0 && stack[len(stack)-1] > num[i] {
			k--
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, num[i])
	}
    stack = stack[:len(stack)-k]
	var zeros int
	for i := range stack {
		if stack[i] != '0' {
			break
		}
		zeros++
	}
    if len(stack) == 0 || zeros == len(stack) {
		return "0"
	}
	return string(stack[zeros:])
}

