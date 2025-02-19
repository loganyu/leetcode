'''
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.



Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.


Constraints:

1 <= num1, num2 <= 109
'''

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = num1

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = bin(result).count("1")
        current_bit = 0
        while set_bits_count < target_set_bits_count:
            if not self._is_set(result, current_bit):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit += 1

        while set_bits_count > target_set_bits_count:
            if self._is_set(result, current_bit):
                result = self._unset_bit(result, current_bit)
                set_bits_count -= 1
            current_bit += 1

        return result

    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)

    def _unset_bit(self, x: int, bit: int):
        return x & ~(1 << bit)

