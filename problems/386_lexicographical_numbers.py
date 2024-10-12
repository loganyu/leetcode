'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.



Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]


Constraints:

1 <= n <= 5 * 104
'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        current_number = 1
        for _ in range(n):
            lexicographical_numbers.append(current_number)
            if current_number * 10 <= n:
                current_number *= 10
            else:
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10
                current_number += 1

        return lexicographical_numbers

