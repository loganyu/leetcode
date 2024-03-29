/*
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
*/

func subarraySum(nums []int, k int) int {
    sumCount := make(map[int]int)
    sumCount[0] = 1
    sum := 0
    count := 0
    for i := 0; i < len(nums); i++ {
        sum += nums[i]
        count += sumCount[sum - k]
        sumCount[sum]++
    }
    
    return count
}

