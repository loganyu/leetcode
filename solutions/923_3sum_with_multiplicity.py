'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
'''

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        arr.sort()
        
        for i, num in enumerate(arr):
            total = target - num
            j, k = i+1, len(arr) - 1
            while j < k:
                if arr[j] + arr[k] < total:
                    j += 1
                elif arr[j] + arr[k] > total:
                    k -= 1
                elif arr[j] != arr[k]:
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        right += 1
                        k -= 1
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1
                else:
                    ans += (k-j+1) * (k-j) // 2
                    ans %= MOD
                    break
        
        return ans
    
