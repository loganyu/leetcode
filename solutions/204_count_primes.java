/*
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
*/

class Solution {
    public int countPrimes(int n) {
        if (n <= 2)
            return 0;
        
        boolean[] numbers = new boolean[n];
        for (int p = 2; p <= (int) Math.sqrt(n); p++)
            if (numbers[p] == false)
                for (int j = p*p; j < n; j += p)
                    numbers[j] = true;
        
        int numberOfPrimes = 0;
        for (int i = 2; i < n; i++)
            if (numbers[i] == false)
                numberOfPrimes++;
        
        return numberOfPrimes;
    }
}

