'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].



Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.


Constraints:

1 <= left <= right <= 106
'''

class Solution:
    def _is_prime(self, number: int) -> bool:
        if number == 1:
            return False
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime_numbers = []

        for candidate in range(left, right + 1):
            if candidate % 2 == 0 and candidate > 2:
                continue
            if self._is_prime(candidate):
                if prime_numbers and candidate <= prime_numbers[-1] + 2:
                    return [prime_numbers[-1], candidate]
                prime_numbers.append(candidate)

        if len(prime_numbers) < 2:
            return [-1, -1]

        closest_pair = [-1, -1]
        min_difference = 1e6
        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = [prime_numbers[index - 1], prime_numbers[index]]

        return closest_pair

