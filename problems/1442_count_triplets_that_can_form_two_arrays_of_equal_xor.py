'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.



Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10


Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        size = len(arr)
        count = 0
        prefix = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        total_map = defaultdict(int)
        for i in range(size):
            prefix ^= arr[i]
            count += count_map[prefix] * i - total_map[prefix]
            total_map[prefix] += i + 1
            count_map[prefix] += 1

        return count

