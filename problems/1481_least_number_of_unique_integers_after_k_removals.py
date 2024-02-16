'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        map = {}
        for i in arr:
            map[i] = map.get(i, 0) + 1
        n = len(arr)
        count_of_frequencies = [0] * (n + 1)
        for count in map.values():
            count_of_frequencies[count] += 1
        remaining_unique_elements = len(map)
        for i in range(1, n + 1):
            num_elements_to_remove = min(k // i, count_of_frequencies[i])
            k -= (i * num_elements_to_remove)
            remaining_unique_elements -= num_elements_to_remove
            if k < i:
                return remaining_unique_elements
        return 0

