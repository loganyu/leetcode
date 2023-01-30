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

func sequentialDigits(low int, high int) []int {
    d, ans := "123456789", []int{}
    l, h := len(strconv.Itoa(low)), len(strconv.Itoa(high))
    for i := l; i <= h; i++ {
        for j := 0; j < 10 - i; j++ {
            n, _ := strconv.Atoi(d[j:j+i])
            if n >= low && n <= high {
                ans = append(ans, n)
            }
        }
    }
    
    return ans
}

